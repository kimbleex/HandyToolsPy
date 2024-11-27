# -*- coding: utf-8 -*-
from collections import Counter
from typing import Union, List, Dict
import pandas as pd

class DataProcess:
    def count_words_freq(words: Union[List[str], pd.DataFrame], sort_methods: str = "DESC") -> Dict[str, int]:
        """
        Count the frequency of words and sort the result by frequency.
        
        :param words: List of words or a DataFrame with one column of words.
        :type words: Union[List[str], pd.DataFrame]
        :param sort_methods: "ASC" or "DESC" for sort sequence, default is "DESC"
        :type sort_methods: str
        :return: Dictionary of word frequencies sorted by frequency.
        :rtype: Dict[str, int]
        """
        if isinstance(words, pd.DataFrame):
            if words.shape[1] != 1:
                raise ValueError("DataFrame must have only one column")
            words = words.iloc[:, 0].tolist()

        words_freq = Counter(words)
        sorted_words_freq = dict(sorted(words_freq.items(), key=lambda x: x[1], reverse=(sort_methods == "DESC")))
        
        return sorted_words_freq
