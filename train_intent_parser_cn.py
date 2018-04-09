#!/usr/bin/env python
# coding: utf-8
"""Using the parser to recognise your own semantics

spaCy's parser component can be used to trained to predict any type of tree
structure over your input text. You can also predict trees over whole documents
or chat logs, with connections between the sentence-roots used to annotate
discourse structure. In this example, we'll build a message parser for a common
"chat intent": finding local businesses. Our message semantics will have the
following types of relations: ROOT, PLACE, QUALITY, ATTRIBUTE, TIME, LOCATION.

"show me the best hotel in berlin"
('show', 'ROOT', 'show')
('best', 'QUALITY', 'hotel') --> hotel with QUALITY best
('hotel', 'PLACE', 'show') --> show PLACE hotel
('berlin', 'LOCATION', 'hotel') --> hotel with LOCATION berlin

Compatible with: spaCy v2.0.0+
"""
from __future__ import unicode_literals, print_function

import plac
import random
import spacy
from pathlib import Path


# training data: texts, heads and dependency labels
# for no relation, we simply chose an arbitrary dependency label, e.g. '-'
TRAIN_DATA = [
    ("找无线质量好的咖啡厅", {
        'heads': [0, 5, 1, 2, 5, 0, 333, 333, 333, 333],  # index of token head
        'deps': ['ROOT', 'ATTRIBUTE', 'ATTRIBUTE', 'QUALITY', '-', 'PLACE', '-', '-', '-', '-']
    }),
    ("找一个靠近海边的酒店", {
        'heads': [0, 5, 3, 5, 5, 0, 333, 333, 333, 333],
        'deps': ['ROOT', '-', 'QUALITY', 'ATTRIBUTE', '-', 'PLACE', '-', '-', '-', '-']
    }),
    ("给我找一个最近的关门晚的健身房", {
        'heads': [2, 2, 2, 9, 9, 9, 7, 9, 9, 2, 333, 333, 333, 333, 333],
        'deps': ['-', '-', 'ROOT', '-', 'QUALITY', '-', 'TIME', 'ATTRIBUTE', '-', 'PLACE', '-', '-', '-', '-', '-']
    }),
    ("告诉我最便宜的卖花的商店", {
        'heads': [0, 0, 3, 7, 7, 7, 7, 0, 333, 333, 333, 333],  # attach "flowers" to store!
        'deps': ['ROOT', '-', 'QUALITY', 'ATTRIBUTE', '-', 'PRODUCT', '-', 'PLACE', '-', '-', '-', '-']
    }),
    ("找一个在伦敦的好餐厅", {
        'heads': [0, 6, 3, 6, 6, 6, 0, 333, 333, 333],
        'deps': ['ROOT', '-', '-', 'LOCATION', '-', 'QUALITY', 'PLACE', '-', '-', '-']
    }),
    ("告诉我在柏林最酷的旅社", {
        'heads': [0, 0, 3, 6, 6, 6, 0, 333, 333, 333, 333],
        'deps': ['ROOT', '-', '-', 'LOCATION', 'QUALITY', '-', 'PLACE', '-', '-', '-', '-']
    }),
    ("找一个上班近的好的意大利餐厅", {
        'heads': [0, 8, 3, 8, 8, 8, 8, 8, 0, 333, 333, 333, 333, 333],
        'deps': ['ROOT', '-', 'LOCATION', 'ATTRIBUTE', '-', 'QUALITY', '-', 'ATTRIBUTE', 'PLACE', '-', '-', '-', '-', '-']
    })
]


@plac.annotations(
    model=("Model name. Defaults to blank 'en' model.", "option", "m", str),
    output_dir=("Optional output directory", "option", "o", Path),
    n_iter=("Number of training iterations", "option", "n", int))
def main(model=None, output_dir=None, n_iter=5):
    """Load the model, set up the pipeline and train the parser."""
    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank('en')  # create blank Language class
        print("Created blank 'en' model")

    # We'll use the built-in dependency parser class, but we want to create a
    # fresh instance – just in case.
    if 'parser' in nlp.pipe_names:
        nlp.remove_pipe('parser')
    parser = nlp.create_pipe('parser')
    nlp.add_pipe(parser, first=True)

    for text, annotations in TRAIN_DATA:
        for dep in annotations.get('deps', []):
            parser.add_label(dep)

    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'parser']
    with nlp.disable_pipes(*other_pipes):  # only train parser
        optimizer = nlp.begin_training()
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            losses = {}
            for text, annotations in TRAIN_DATA:
                nlp.update([text], [annotations], sgd=optimizer, losses=losses)
            print(losses)

    # test the trained model
    test_model(nlp)

    # save model to output directory
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

        # test the saved model
        print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        test_model(nlp2)


def test_model(nlp):
    texts = ["找一个上班近的好的意大利餐厅"]
    docs = nlp.pipe(texts)
    for doc in docs:
        print(doc.text)
        print([(t.text, t.dep_, t.head.text) for t in doc if t.dep_ != '-'])


if __name__ == '__main__':
    plac.call(main)

    # Expected output:
    # find a hotel with good wifi
    # [
    #   ('find', 'ROOT', 'find'),
    #   ('hotel', 'PLACE', 'find'),
    #   ('good', 'QUALITY', 'wifi'),
    #   ('wifi', 'ATTRIBUTE', 'hotel')
    # ]
    # find me the cheapest gym near work
    # [
    #   ('find', 'ROOT', 'find'),
    #   ('cheapest', 'QUALITY', 'gym'),
    #   ('gym', 'PLACE', 'find')
    #   ('work', 'LOCATION', 'near')
    # ]
    # show me the best hotel in berlin
    # [
    #   ('show', 'ROOT', 'show'),
    #   ('best', 'QUALITY', 'hotel'),
    #   ('hotel', 'PLACE', 'show'),
    #   ('berlin', 'LOCATION', 'hotel')
    # ]
