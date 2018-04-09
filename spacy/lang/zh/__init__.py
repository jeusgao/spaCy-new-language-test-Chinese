# coding: utf8
from __future__ import unicode_literals

from .tag_map import TAG_MAP
from .stop_words import STOP_WORDS
from .lex_attrs import LEX_ATTRS
from .morph_rules import MORPH_RULES
from .syntax_iterators import SYNTAX_ITERATORS

from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ..norm_exceptions import BASE_NORMS
from ..punctuation import TOKENIZER_PREFIXES, TOKENIZER_SUFFIXES, TOKENIZER_INFIXES
from ..char_classes import UNITS, CURRENCY, QUOTES, PUNCT, HYPHENS, ICONS, LIST_UNITS, LIST_CURRENCY, LIST_QUOTES, LIST_PUNCT, LIST_HYPHENS, LIST_ELLIPSES, LIST_ICONS

from ...attrs import LANG, NORM
from ...language import Language
from ...tokens import Doc
from ...util import update_exc, add_lookups


class ChineseDefaults(Language.Defaults):
    lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    lex_attr_getters.update(LEX_ATTRS)
    lex_attr_getters[LANG] = lambda text: 'zh'  # for pickling
    lex_attr_getters[NORM] = add_lookups(Language.Defaults.lex_attr_getters[NORM],
                                         BASE_NORMS)
    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS)

    use_jieba = True
    tag_map = TAG_MAP
    stop_words = STOP_WORDS
    morph_rules = MORPH_RULES
    syntax_iterators = SYNTAX_ITERATORS


class Chinese(Language):
    lang = 'zh'
    Defaults = ChineseDefaults  # override defaults

    def make_doc(self, text):
        if self.Defaults.use_jieba:
            try:
                import jieba
            except ImportError:
                msg = ("Jieba not installed. Either set Chinese.use_jieba = False, "
                       "or install it https://github.com/fxsjy/jieba")
                raise ImportError(msg)
            words = list(jieba.cut(text, cut_all=False))
            words = [x for x in words if x]
            return Doc(self.vocab, words=words, spaces=[False]*len(words))
        else:
            words = []
            spaces = []
            doc = self.tokenizer(text)
            for token in self.tokenizer(text):
                words.extend(list(token.text))
                spaces.extend([False]*len(token.text))
                spaces[-1] = bool(token.whitespace_)
            return Doc(self.vocab, words=words, spaces=spaces)


__all__ = ['Chinese']
