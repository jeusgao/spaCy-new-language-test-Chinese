# coding: utf8
from __future__ import unicode_literals

from ...symbols import LEMMA, PRON_LEMMA


MORPH_RULES = {
    "PRP": {
        "我":           {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "One", "Number": "Sing"},
        "你":           {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "Two"},
        "他":           {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "Three", "Number": "Sing", "Gender": "Masc"},
        "她":           {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "Three", "Number": "Sing", "Gender": "Fem"},
        "它":           {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "Three", "Number": "Sing", "Gender": "Neut"},
        "我们":         {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "One", "Number": "Plur"},
        "他们":         {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "Three", "Number": "Plur", "Gender": "Masc"},
        "她们":         {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "Three", "Number": "Plur", "Gender": "Fem"},

        "我的":          {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "One", "Number": "Sing", "Poss": "Yes", "Reflex": "Yes"},
        "他的":          {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "Three", "Number": "Sing", "Gender": "Masc", "Poss": "Yes", "Reflex": "Yes"},
        "她的":          {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "Three", "Number": "Sing", "Gender": "Fem",  "Poss": "Yes", "Reflex": "Yes"},
        "它的":          {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "Three", "Number": "Sing", "Gender": "Neut", "Poss": "Yes", "Reflex": "Yes"},
        "我们的":        {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "One", "Number": "Plur", "Poss": "Yes", "Reflex": "Yes"},
        "你们的":        {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "Two", "Number": "Plur", "Poss": "Yes", "Reflex": "Yes"},
        "他们的":        {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "Three", "Number": "Plur", "Poss": "Yes", "Reflex": "Yes"},
        "她们的":        {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "Three", "Number": "Plur", "Gender": "Fem", "Poss": "Yes", "Reflex": "Yes"},

        "我自己":        {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "One", "Number": "Sing",  "Case": "Acc", "Reflex": "Yes"},
        "你自己":        {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "Two", "Case": "Acc", "Reflex": "Yes"},
        "他自己":        {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "Three", "Number": "Sing", "Case": "Acc", "Gender": "Masc", "Reflex": "Yes"},
        "她自己":        {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "Three", "Number": "Sing", "Case": "Acc", "Gender": "Fem",  "Reflex": "Yes"},
        "它自己":        {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "Three", "Number": "Sing", "Case": "Acc", "Gender": "Neut", "Reflex": "Yes"},
        "他们自己":      {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "Three", "Number": "Sing", "Case": "Acc", "Reflex": "Yes"},
        "她们自己":      {LEMMA: PRON_LEMMA, "PronType": "Prs", "Person": "Three", "Number": "Sing", "Case": "Acc", "Gender": "Fem","Reflex": "Yes"},
    },

    "PRP$": {
        "我的":          {LEMMA: PRON_LEMMA, "Person": "One", "Number": "Sing", "PronType": "Prs", "Poss": "Yes"},
        "你的":          {LEMMA: PRON_LEMMA, "Person": "Two", "PronType": "Prs", "Poss": "Yes"},
        "他的":          {LEMMA: PRON_LEMMA, "Person": "Three", "Number": "Sing", "Gender": "Masc", "PronType": "Prs", "Poss": "Yes"},
        "她的":          {LEMMA: PRON_LEMMA, "Person": "Three", "Number": "Sing", "Gender": "Fem",  "PronType": "Prs", "Poss": "Yes"},
        "它的":          {LEMMA: PRON_LEMMA, "Person": "Three", "Number": "Sing", "Gender": "Neut", "PronType": "Prs", "Poss": "Yes"},
        "我们的":        {LEMMA: PRON_LEMMA, "Person": "One", "Number": "Plur", "PronType": "Prs", "Poss": "Yes"},
        "他们的":        {LEMMA: PRON_LEMMA, "Person": "Three", "Number": "Plur", "PronType": "Prs", "Poss": "Yes"},
        "她们的":        {LEMMA: PRON_LEMMA, "Person": "Three", "Number": "Plur", "PronType": "Prs", "Gender": "Fem", "Poss": "Yes"}
    },

    "VBZ": {
        "是":           {LEMMA: "be", "VerbForm": "Fin", "Tense": "Pres", "Mood": "Ind"},
        "为":           {LEMMA: "be", "VerbForm": "Fin", "Tense": "Pres", "Mood": "Ind"},
    },
}


for tag, rules in MORPH_RULES.items():
    for key, attrs in dict(rules).items():
        rules[key.title()] = attrs
