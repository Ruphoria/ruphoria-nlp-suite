"""This module handles the recovery of words that may have been misparsed or misspelled.
"""
# Actual service dependencies
import itertools
import os
import re
import wordninja
import numpy as np
import pandas as pd

from enchant.checker import SpellChecker
from joblib import Memory

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.metrics.distance import edit_distance
from scipy.stats import rankdata
import redis

from wb_cleaning.cleaning.stopwords import stopwords
from wb_cleaning import dir_manager
from wb_cleaning.interfaces import language
# Setup caching mechanism for speedup.
# Take note that `get_suggestions` using enchant is
# quite slow (~75% of the `cached_infer_correct_word` function).

USE_JOBLIB_MEMORY = False
# EN_DICT = None

if not USE_JOBLIB_MEMORY:
    try:
        from wb_cleaning.ops.cache_utils import redis_cacher
        cache_decorator = redis_cacher

    except redis.ConnectionError as error:
        args = error.args
        print(args[0])
        print("Redis not available, falling back to joblib cache...")
        USE_JOBLIB_MEMORY = True

if USE_JOBLIB_MEMORY:
    RESPELLER_CACHE_LOCATION = "/dev/shm/respeller-cachedir"

    try:
        respeller_cache = Memory(RESPELLER_CACHE_LOCATION, verbose=0)
    except PermissionError:
        RESPELLER_CACHE_LOCATION = dir_manager.get_data_dir(
            'shm', 'respeller-cachedir')

        if not os.path.isdir(RESPELLER_CACHE_LOCATION):
            os.makedirs(RESPELLER_CACHE_LOCATION)

        respeller_cache = Memory(RESPELLER_CACHE_LOCATION, verbose=0)

    cache_decorator = respeller_cache.cache

# # Returns self without any form of caching.
# cache_decorator = lambda f: f

#
# en_dict = language.Language().get_en_dict()
en_lang = language.Language()


# def get_dict():
#     # Use this since DictWithPWL fails when pickled/unpickled
#     global EN_DICT
#     if EN_DICT is None:
#         EN_DICT = language.Language().get_en_dict()
#     return EN_DICT

# with open(dir_manager.get_data_dir("whitelists", "whitelists", "whitelist_words.txt")) as whitelist_words_file:

#     for word in whitelist_words_file.readlines():
#         word = word.strip()

#         # add word to personal dictionary
#         # en_us.add(word)

#         # add word just for this session
#         en_dict.add_to_session(word)


@cache_decorator
def get_suggestions(word: str, **kwargs) -> list:
    """Wrapper the caches the result of enchant's suggest method.

    Args:
        word:
            Word to check for suggestions.

    Returns:
        A list containing the most likely correct words based on enchant's dictionary.

    """

    if en_lang.get_en_dict().check(word):
        suggest = [word]
    else:
        suggest = en_lang.get_en_dict().suggest(word)

    return suggest


# @cache_decorator
# def en_dict_check(word, **kwargs):
#     # High overhead. Uncached speed ~100us vs cached speed ~500us
#     return en_dict.check(word)


def morph_word(word: str) -> str:
    """Apply simple morphing of the word to improve robustness for checking similarity.

    A derived token is created by concatenating the word and the sorted version of the word.

    Args:
        word:
            Word to be morphed.

    Returns:
        The morphed word.

    """
    # word = word.replace(' ', '')  # Check if compound word suggestion matches the misspelled word
    # Perform this opperation to add more robustness to the matching
    # m_word = word + "".join(sorted(word))
    m_word = word

    return m_word


@cache_decorator
def cached_infer_correct_word(
        word: str, sim_thresh: float = 0.0, print_log: bool = False,
        min_len: int = 3, use_suggest_score: bool = True, **kwargs) -> dict:
    """This method computes the inference score for the input word.

    Args:
        word:
            This is the misspelled word that requires checking for fix.
        sim_thresh:
            Similarity threshold to use to check if the candidate is
            acceptable.
            The similarity is derived based on character similarity
            and rank based on enchant's suggestions.
        print_log:
            Option to print the payload.
        min_len:
            Minimum length of token to check.
            If less than the `min_len`, don't attempt to fix.
        use_suggest_score:
            Flag whether to use the rank of enchant's suggestion in
            computing for the similarity score.
        **kwargs:
            Needed for caching (`argument_hash`)

    Returns:
        A dictionary containing the information of the inference.

    """
    # To collect cached data, execute the line below.
    # redis.hgetall('cleaner/respelling/cached_infer_correct_word')
    correct_word = None
    score = -1

    payload = dict(
        word=word,
        correct_word=correct_word,
        score=score,
        sim_thresh=sim_thresh,
        print_log=print_log,
        min_len=min_len,
        