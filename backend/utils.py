"""
This file is for small stand alone functions
"""
from random_word import RandomWords


# TODO: Improve this function to get more meaningful words!
# It could be anything: famous people, car models, colors, a place in the world,
# this is very very very very very very very important so
# that the story is entertaining and most importantly CREATIVE
# This function is used in get_the_word_for_the_blank
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

