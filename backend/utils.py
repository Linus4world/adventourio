"""
This file is for small stand alone functions
"""
import urllib.request
import random
import pycorpora
from random_word import RandomWords

#Here be global variables
adventurer_treasure = ["Crystal Skull", "Monkey Statue", "Stuffed Wolpertinger", "Ancient Porn Magazine",
                       "Long-Lost Martian Technology", "Hoard of Gold", "Creepy Medieval Painting", "Golden Globe",
                       "Holy Grail", "Perpetuum Mobile"]

adventurer_map = ["Legendary Map", "Ancient Scroll", "Mysterious Hieroglyphs", "Wise GPS System",
                  "Ominous Road Sign", "Misleading Pictogram Panel", "Tacky Compass", "Sarcastic Recommendation",
                  "Letter Of A Lost Lover", "Battered Postcard"]

sci_fi_thing = ["Sonic Screwdriver", "Flux Capacitative Transcriber", "Bionic Sewing Needle", "Alpha ray excavator",
                "Chromospheric Sensation Cord", "Cepheid Variability Oscillator", "Ceolostatic Clockwork",
                "Cybernetic Bottleneck", "Diurnal Dynamite Mug", "Homunculoid Electrowaiver"]
magic_thing = ["Ring", "Amulet", "Toe ring", "Nose ring", "Earring", "Necklace", "Book", "Staff", "Wand", "Cloak"]

detective_weapon = ["Shotgun", "Plasma rifle", "Trusty Fists", "Unbreakable Katana Sword", "Machete", "Dagger",
                    "Revolver", "Legendary Broadsword", "Pistol", "Scythe"]

assigned_keywords = {} #dictionary with keyword:value


rw = RandomWords()
word_site = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = urllib.request.urlopen(word_site)
long_txt = response.read().decode()
words = long_txt.splitlines()


# TODO: Improve this function to get more meaningful words!
# It could be anything: famous people, car models, colors, a place in the world,
# this is very very very very very very very important so
# that the story is entertaining and most importantly CREATIVE
# This function is used in get_the_word_for_the_blank

def get_random_word_from_the_internet(part_of_speech):
    return rw.get_random_word(hasDictionaryDef="true",
                              # includePartOfSpeech='adjective',
                              includePartOfSpeech=part_of_speech,
                              minCorpusCount=50,
                              minDictionaryCount=1,
                              maxDictionaryCount=50,
                              minLength=5,
                              maxLength=10)

def get_random_name():
    first_name = rw.random_nick(gender='m')
    upper_words = [word for word in words if word[0].isupper()]
    name_words  = [word for word in upper_words if not word.isupper()]
    name = ' '.join([name_words[random.randint(0,len(name_words))] for i in range(2)])
    return name


# Mock json for testing the character assignment
answers1 = """
{
    "all_answers": [
        {
            "id": "1",
            "answers": [
                "a",
                "a",
                "d",
                "d"
            ]
        },
        {
            "id": "2",
            "answers": [
                "a",
                "b",
                "b",
                "c"
            ]
        },
        {
            "id": "3",
            "answers": [
                "b",
                "c",
                "a",
                "a"
            ]
        },
        {
            "id": "4",
            "answers": [
                "b",
                "c",
                "b",
                "b"
            ]
        }
    ]
}
"""
answers2 = """
{
    "all_answers": [
        {
            "id": "1",
            "name": "ja",
            "answers": [
                "a",
                "a",
                "a",
                "d",
                "c",
                "d",
                "b"
            ]
        },
        {
            "id": "2",
            "name": "ja2",
            "answers": [
                "a",
                "a",
                "a",
                "d",
                "c",
                "d",
                "b"
            ]
        },
        {
            "id": "3",
            "name": "ja3",
            "answers": [
                "a",
                "a",
                "a",
                "a",
                "b",
                "b",
                "c"
            ]
        },
        {
            "id": "4",
            "name": "ja4",
            "answers": [
                "a",
                "a",
                "a",
                "b",
                "c",
                "b",
                "b"
            ]
        }
    ]
}
"""
answers3 = """
{
    "all_answers": [
        {
            "id": "1",
            "name": "ja",
            "answers": [
                "a",
                "a",
                "a",
                "a",
                "b",
                "c",
                "d"
            ]
        },
        {
            "id": "2",
            "name": "ja2",
            "answers": [
                "a",
                "a",
                "a",
                "a",
                "b",
                "c",
                "d"
            ]
        },
        {
            "id": "3",
            "name": "ja3",
            "answers": [
                "a",
                "a",
                "a",
                "c",
                "a",
                "c",
                "d"
            ]
        },
        {
            "id": "4",
            "name": "ja4",
            "answers": [
                "a",
                "a",
                "a",
                "d",
                "b",
                "b",
                "c"
            ]
        }
    ]
}
"""
