"""
This file is for small stand alone functions
"""
from random_word import RandomWords


def get_random_word_from_the_internet(part_of_speech):
    rw = RandomWords()
    return rw.get_random_word(hasDictionaryDef="true",
                              # includePartOfSpeech='adjective',
                              includePartOfSpeech=part_of_speech,
                              minCorpusCount=50,
                              minDictionaryCount=1,
                              maxDictionaryCount=50,
                              minLength=5,
                              maxLength=10)