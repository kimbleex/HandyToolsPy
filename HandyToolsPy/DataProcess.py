# -*- coding: utf-8 -*-

from collections import Counter
from pandas import DataFrame
from typing import Union

def count_words_freq(words : Union[list, DataFrame], sort_methods: str = "DESC") -> dict:
    """
    Only One column of DataFrame is allowed
    
    :param words: list of words
    :type words: list
    :param sort_choice: "ASC" or "DESC" for sort sequence, default is "DESC"
    :type sort_choice: str
    """
    if type(words) == DataFrame:
        words = list(words)
    words_freq = Counter(words)
    words_freq = dict(sorted(words_freq.items(), key=lambda x: x[1], reverse= True if sort_methods == "DESC" else False))
    return words_freq
