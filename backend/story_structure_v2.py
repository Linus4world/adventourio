import numpy as np
import time
import random
import json
import re
from utils import *
from story_telling import *
import pycorpora


class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.story_row = -1


class Story:
    """
    Attributes:
        pages (np.ndarray): pages is a nxm matrix of type Page()
        challenges (dict):
        blanks (dict):
    """

    def __init__(self, story_size):
        n = story_size[0]
        m = story_size[1]
        # pages is a nxm matrix of type Page()
        pages = np.zeros((n, m), dtype=Page)
        # Each element of the matrix is initialized
        for row in range(n):
            for column in range(m):
                pages[row, column] = Page()

        self.story_size = story_size

        self.pages = pages
        self.blanks = {}
        self.characters = []
        self.challenges = {}

    # --------------- SET UP: ---------------

    def setup_story(self):

        # Add content of the story
        set_example_story(self)

    # --------------- CHARACTERS: ---------------

    def add_character(self, name, description):
        character = Character(name, description)
        character.story_row = len(self.characters)
        self.characters.append(character)

    def get_character(self, character_name):
        for character in self.characters:
            if character.name == character_name:
                return character

    def get_character_story_row(self, character_name):
        """
        pages is a matrix.
        Each character has a row in the pages matrix assigned

        Parameters:
            character_name (str):
        Returns:
            idx (int): his function returns the row that corresponds to the character
        """
        # for character in self.characters:
        #     print(character.name, end=' ')
        # print("")

        for idx, character in enumerate(self.characters):
            if character.name == character_name:
                return idx

    # --------------- CHALLENGES: ---------------

    def load_all_challenges(self, challenges_json):
        with open(challenges_json) as json_file:
            challenges = json.load(json_file)
        self.challenges.update(challenges)

    def add_challenge(self, challenge_id, challenge):
        self.blanks[challenge_id] = challenge

    def get_challenge(self, challenge_id):
        return self.challenges[challenge_id]

    # --------------- BLANKS: ---------------

    def add_blank(self, blank_id, word_type="None", changes_every_time=False, list_of_words=None):
        """
        Parameters:
            blank_id (str):
            (list_of_words (list of str): possible words to fill in the blank with)
            word_type(str): what category of word is this (flower, spell, etc), has to fit with json file names in pycorpora
            changes_every_time (bool): if the blank should be filled in with a (potentially) different word every time
            list_of_words
        """
        blank = dict(
            changes_every_time=changes_every_time,
            list_of_words=list_of_words,
            word_type=word_type
        )
        self.blanks[blank_id] = blank

#    def add_blank_internet(self, blank_key, part_of_speech, changes_every_time=False):
#        """
#        Parameters:
#            blank_key (str):
#            part_of_speech (str): noun, adjective, etc.
#            changes_every_time (bool): if the blank should be filled in with a (potentially) different word every time
#        """
#        blank = dict(
#            random_word=True,
#            part_of_speech=part_of_speech,
#            changes_every_time=changes_every_time
#        )
#        self.blanks[blank_key] = blank

    # def get_the_word_for_the_blank(self, blank_id):
    #     return 'boobs'

    def get_the_word_for_the_blank(self, blank_id):
        """
        Description: It uses the blank to find a word to fill it with

        Parameters:
             blank_id:

        Returns:
            A word with which the blank will be filled
        """
        """
        Keyword blanks have to be called: treasure, map, tech, magic, weapon
        """

        blank = self.blanks[blank_id]
        # Random word from the internet!
        if blank['changes_every_time']:
            """
            In this case we replace the word with something from pycorpora
            Check word types
            """
            if blank_id == "spells":
                return random.choice(pycorpora.words.spells['spells'])['incantation']
            elif blank_id == "adverbs":
                return random.choice(pycorpora.words.adverbs['adverbs'])
            elif blank_id == "nouns":
                return random.choice(pycorpora.words.nouns['nouns'])
            elif blank_id == "strange_words":
                return random.choice(pycorpora.words.strange_words['words'])
            elif blank_id == "lovecraft_words":
                return random.choice(pycorpora.words.literature.lovecraft_words['words'])
            elif blank_id == "shakespeare_words":
                return random.choice(pycorpora.words.literature.shakespeare_words['words'])
            else:
                return "you messed up, buddy"  # LOL

        #    part_of_speech = blank['part_of_speech']
        #    word = get_random_word_from_the_internet(part_of_speech)
        # Random word from the list of words provided
        else:
            # list_of_words = self.blanks[blank_key]['list_of_words']
            # word = random.choice(list_of_words)
            if blank_id not in assigned_keywords:
                if blank_id == "treasure":
                    treasure = random.choice(adventurer_treasure)
                    assigned_keywords["treasure"] = treasure
                    return treasure
                elif blank_id == "map":
                    map = random.choice(adventurer_map)
                    assigned_keywords["map"] = map
                    return map
                elif blank_id == "tech":
                    tech = random.choice(sci_fi_thing)
                    assigned_keywords["tech"] = tech
                    return tech
                elif blank_id == "magic":
                    magic = random.choice(magic_thing)
                    assigned_keywords["magic"] = magic
                    return magic
                elif blank_id == "weapon":
                    weapon = random.choice(detective_weapon)
                    assigned_keywords["weapon"] = weapon
                    return weapon
            else:
                return assigned_keywords[blank_id]

    def fill_in_the_blanks(self, page_variation):
        """
        Fills in all the blanks in a page_variation
        """
        ret_txt = []
        for txt in page_variation.txt:
            found_keys = re.findall(r'~\w+~', txt)
            for blank_key in found_keys:
                print(blank_key)
                if blank_key[1:-1] in self.blanks.keys():
                    word = self.get_the_word_for_the_blank(blank_key[1:-1])
                    txt = txt.replace(blank_key, word)
            ret_txt.append(txt)
        return ret_txt

    # --------------- OUTCOME SELECTION: ---------------

    @staticmethod
    def select_good_or_bad_outcome(page_variations, player):
        """
        Description: It uses the blank to find a word to fill it with

        Parameters:
             page_variations (array of PageVariation):
             player (Player):

        Returns:
            ret_page_variation (PageVariation): One of the page variations from the page_variations array
        """

        challenge_outcomes = player.challenge_outcomes
        challenge_outcome = challenge_outcomes[-1]  # Outcome of last challenge
        prob_array = player.prob_array
        good_outcome = page_variations[0]
        bad_outcome = page_variations[1]

        # prob_array is a list of tuples like [(0.82, "good"), (0.63, "bad")]
        total_val = 0.0
        rand_num = round(random.uniform(-1, 1), 2)
        # all calculations performed for probability to get good event
        challenge_outcome = int(challenge_outcome)
        good_probability = max(min(challenge_outcome + rand_num, 1), 0)
        for el in prob_array:
            if el[1] == "bad":
                val = -1 * el[0]
            else:
                val = el[0]
            total_val = total_val + val
        good_probability = max(min(good_probability + total_val, 1), 0)
        if good_probability >= 0.5:
            prob_array.append((good_probability, "good"))
            ret_page_variation = good_outcome  # Returned page variation
        else:
            # gets probability for bad event
            prob_array.append((1-good_probability, "bad"))
            ret_page_variation = bad_outcome  # Returned page variation

        return ret_page_variation

    # --------------- PAGE ADDRESSING: ---------------

    def get_page_raw(self, row, column):
        return self.pages[row][column]

    def get_page(self, character_name, chapter, page):
        """
        Parameters:
            character_name (str):
            chapter (int): A chapter consists of 3 pages
            page (str): Can only be {0, 1, 2}
        Returns:
            The page at specified location
        """
        row = self.get_character_story_row(character_name)
        page_number = {'intro': 0, 'challenge': 1, 'outro': 2}
        column = chapter * 3 + page_number[page]
        return self.pages[row][column]


class Page:
    def __init__(self):
        self.page_name = ''
        self.page_variations = []
        self.page_type = ''
        self._last_page = False

    def add_page_variation(self, txt=None, challenge=None):
        page_var = PageVariation()
        page_var.txt = txt
        page_var.challenge = challenge
        self.page_variations.append(page_var)

    def set_page_type(self, page_type):
        correct_page_type = page_type == 'challenge' or page_type == 'outcome'
        assert correct_page_type, 'page_type must be equal to \'challenge\' or \'outcome\''
        self.page_type = page_type

    def set_last_page(self, last_page_bool):
        self._last_page = last_page_bool

    def is_it_the_last_page(self):
        return self._last_page


class PageVariation:
    """
    Attributes:
        txt (list of strings): Contains the story content
    """

    def __init__(self):
        self.txt = []
        self.challenge = {}
        self.story_location = [0, 0, 0]
