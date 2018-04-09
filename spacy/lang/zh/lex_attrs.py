# coding: utf8
from __future__ import unicode_literals

from ...attrs import LIKE_NUM


_num_words = ['零', '一', '二', '三', '四', '五', '六', '七',
              '八', '九', '十', '十一', '十二', '十三', '十四',
              '十五', '十六', '十七', '十八', '十九', '二十',
              '三十', '四十', '五十', '六十', '七十', '八十', '九十',
              '百', '千', '百万', '十亿', '万亿', '百兆',
              'gajillion', 'bazillion']


def like_num(text):
    text = text.replace(',', '').replace('.', '')
    if text.isdigit():
        return True
    if text.count('/') == 1:
        num, denom = text.split('/')
        if num.isdigit() and denom.isdigit():
            return True
    if text.lower() in _num_words:
        return True
    return False


LEX_ATTRS = {
    LIKE_NUM: like_num
}
