import numpy as np
import time
import random
import json
from utils import *
from characters_and_challenges import *


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
        self.pages = pages

        self.challenges = {}
        self.blanks = {}

        self.characters = []

    # --------------- SET UP: ---------------

    def setup_story(self):
        self.add_character(Character(name='adventurer', description='drunk'))
        self.add_character(Character(name='alien', description='academic'))
        self.add_character(Character(name='wizard', description='foreign cultures'))
        self.add_character(Character(name='detective', description='break free'))

    # --------------- CHARACTERS: ---------------

    def add_character(self, character):
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

    def add_blank(self, blank_id, list_of_words, changes_every_time=False):
        """
        Parameters:
            blank_id (str):
            list_of_words (list of str): possible words to fill in the blank with
            changes_every_time (bool): if the blank should be filled in with a (potentially) different word every time
        """
        blank = dict(
            random_word=False,
            list_of_words=list_of_words,
            changes_every_time=changes_every_time
        )
        self.blanks[blank_id] = blank

    def add_blank_random(self, blank_key, part_of_speech, changes_every_time=False):
        """
        Parameters:
            blank_key (str):
            part_of_speech (str): noun, adjective, etc.
            changes_every_time (bool): if the blank should be filled in with a (potentially) different word every time
        """
        blank = dict(
            random_word=True,
            part_of_speech=part_of_speech,
            changes_every_time=changes_every_time
        )
        self.blanks[blank_key] = blank

    def get_the_word_for_the_blank(self, blank_key):
        """
        Description: It uses the blank to find a word to fill it with

        Parameters:
             blank_key:

        Returns:
            A word with which the blank will be filled
        """
        blank = self.blanks[blank_key]
        # Random word from the internet!
        if blank['random_word']:
            part_of_speech = blank['part_of_speech']
            word = get_random_word_from_the_internet(part_of_speech)
        # Random word from the list of words provided
        else:
            list_of_words = self.blanks[blank_key]['list_of_words']
            word = random.choice(list_of_words)
        return word

    def fill_in_the_blanks(self, page_variation):
        """
        Fills in all the blanks in a page_variation
        """
        ret_txt = []  # Text to return
        for txt in page_variation.txt:
            idx_of_blank = txt.find('~')
            if idx_of_blank != -1:
                # Get the blank key
                blank_key = txt[idx_of_blank + 1:idx_of_blank + 4]
                # Blank found!
                if blank_key in self.blanks.keys():
                    # Get the word that will be inserted in the blank
                    word = self.get_the_word_for_the_blank(blank_key)  # get the word t
                    # Replace the blank '~BXX~' for the word
                    txt = txt.replace(txt[idx_of_blank:idx_of_blank + 5], word)
            ret_txt.append(txt)
        return ret_txt

    # --------------- PAGE VARIATION SELECTION: ---------------

    # TODO: AGATA and ESTEBAN [BE-05]
    @staticmethod
    def select_a_challenge(page_variations, player):
        return select_a_challenge(page_variations, player)

    # option choice is dependent on: random number,
    # if players succeeded in LAST task, with what probability the outcomes of the previous stages were selected
    # option choice returns a PROBABILITY to select a good/bad outcome in substage3
    # challenge outcome is 0 for "failed task" and 1 for "achieved task"
    # def select_good_or_bad_outcome(self, challenge_outcome, prob_array):
    # TODO: Sarah and Esteban [BE-07]
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

        player_inputs = player.player_inputs
        challenge_outcome = player_inputs[-1]  # Outcome of last challenge
        prob_array = player.prob_array
        good_outcome = page_variations[0]  # BE FUCKING CAREFUL: THE ORDER IN WHICH YOU STORE THE OUTCOME MATTERS!
        bad_outcome = page_variations[1]  # BE FUCKING CAREFUL: THE ORDER IN WHICH YOU STORE THE OUTCOME MATTERS!

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
            ret_page_variation = bad_outcome # Returned page variation

        return ret_page_variation

    # --------------- PAGE ADDRESSING: ---------------

    def get_page_raw(self, row, column):
        return self.pages[row][column]

    def get_page(self, character_name, chapter, page):
        """
        Parameters:
            character_name (str):
            chapter (int): A chapter consists of 3 pages
            page (int): Can only be {0, 1, 2}
        Returns:
            The page at specified location
        """
        assert 0 <= page <= 2, 'page can only be {0, 1, 2}'
        row = self.get_character_story_row(character_name)
        column = chapter * 3 + page

        return self.pages[row][column]


class Page:
    def __init__(self):
        self.page_name = ''
        self.page_variations = []
        self.page_type = ''

    def add_page_variation(self, txt=None, challenge=None):
        page_var = PageVariation()
        page_var.txt = txt
        page_var.challenge = challenge
        self.page_variations.append(page_var)

    def set_page_type(self, page_type):
        correct_page_type = page_type == 'challenge' or page_type == 'outcome'
        assert correct_page_type, 'page_type must be equal to \'challenge\' or \'outcome\''
        self.page_type = page_type


class PageVariation:
    """
    Attributes:
        txt (list of strings): Contains the story content
    """

    def __init__(self):
        self.txt = []
        self.challenge = {}
        self.story_location = [0, 0, 0]
        self.end_of_story = False

