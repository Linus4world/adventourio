import numpy as np
import time
import random
from utils import *

available_characters = ['alien', 'zombie', 'wizard', 'teacher']


class PlayerError(Exception):
    pass


class Player:

    def __init__(self):
        self.name = ''
        self.player_id = ''
        self.character = ''
        self.story_location = [-1, -1]  # row, column
        self.geo_location = ''
        self.geo_destination = ''
        self.answer = None
        self.game_finished = False

    # TODO: AGATA
    # This function assigns the player a character from the available_characters list
    def assign_character(self):
        # ----- YOUR CODE GOES HERE: -----
        character = random.choice(available_characters)
        # --------------------------------

        self.set_character(character)

    def set_character(self, character):
        """
        Sets the player's character and the story_location.
        The story_location[row] is the index of the character in the available_characters list.

        Parameters:
            character (str): This string has to be on the available_characters list! Otherwise an exception
                will be raised
        """
        if character in available_characters:
            self.character = character
            self.story_location[0] = available_characters.index(character)
        else:
            raise PlayerError('The character ' + character + ' does not exist!')

    def set_story_location(self, story_location):
        """
        Sets player's location

        Parameters:
            story_location (list of 2 ints):
        """
        assert len(story_location) == 2, 'Wrong story location format!'
        self.story_location = story_location

    def get_story_location(self):
        return self.story_location


class Game:
    MAX_WAIT = 50000

    def __init__(self, story_size, max_players=4):
        self.story = Story(story_size)
        self.max_players = max_players
        self.players = []

    def add_player(self, player_id, name, answer):
        player = Player()
        player.name = name
        player.player_id = player_id
        player.answer = answer
        self.players.append(player)

    def is_full(self) -> bool:
        return len(self.players) == self.max_players

    # def get_player_index(self, player_id):
    #     return self.playerIds.index(player_id)

    def get_player(self, player_id):
        """
        Parameters:
            player_id (str):

        Returns:
            Player: Instance of the Player class which has player_id as player id
        """
        for player in self.players:
            if player.player_id == player_id:
                return player

    def wait_for_full_session(self):
        counter = 0
        while counter < self.MAX_WAIT:
            if self.is_full():
                return True
            time.sleep(2)
            counter += 1
        return False

    def get_next_page_variation(self, player_id, player_input):
        # TODO, ADD DOCUMENTATION ABOUT THE player_input
        """
        This function will be constantly called by the frontend to get the next page variation
        Depending on the player, the player.story_location and player_input, the next page variation can be selected

        Parameters:
            player_id (str):
            player_input ():

        Returns:
            PageVariation:
        """
        story = self.story
        player = self.get_player(player_id)
        story_location = player.get_story_location()
        row = story_location[0]
        column = story_location[1]
        page = self.story.get_page_raw(row, column + 1)  # Get the next page

        # TODO: AGATA / SARAH ? [BE-07]
        # ----- YOUR CODE GOES HERE: -----
        page_variation = story.select_page_variation(page.page_variations, player_id, player_input)
        # --------------------------------

        # Filling in the blanks
        page_variation.txt = story.fill_in_the_blanks(page_variation)

        # Set the new location
        player.set_story_location([row, column + 1])
        return page_variation


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

    def add_challenge(self, challenge_key):
        # TODO: AGATA
        # ----- YOUR CODE GOES HERE: -----
        challenge = dict()
        # --------------------------------

        self.blanks['C' + challenge_key] = challenge

    def add_blank(self, blank_key, list_of_words, changes_every_time=False):
        """
        Parameters:
            blank_key (str):
            list_of_words (list of str): possible words to fill in the blank with
            changes_every_time (bool): if the blank should be filled in with a (potentially) different word every time
        """
        blank = dict(
            random_word=False,
            list_of_words=list_of_words,
            keep_initial_word=changes_every_time
        )
        self.blanks['B' + blank_key] = blank

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
            keep_initial_word=changes_every_time
        )
        self.blanks['B' + blank_key] = blank

    def get_the_word_for_the_blank(self, blank_key):
        """
        It uses the blank to find a word to fill it with

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

    # TODO SARAH / AGATA [BE-07]
    def select_page_variation(self, page_variations, player_id, player_input):
        return random.choice(page_variations)  # DUMMY FUNCTION!

    def get_page_raw(self, row, column):
        return self.pages[row][column]

    def get_page(self, character, chapter, page):
        """
        Parameters:
            character (str):
            chapter (int): A chapter consists of 3 pages
            page (int): Can only be {0, 1, 2}
        Returns:
            The page at specified location
        """
        assert 0 <= page <= 2, 'page can only be {0, 1, 2}'
        row = available_characters.index(character)
        column = chapter * 3 + page
        return self.pages[row][column]


class Page:
    def __init__(self):
        self.page_name = ''
        self.page_variations = []

    def add_page_variation(self, txt=None, challenge=None):
        page_var = PageVariation()
        page_var.txt = txt
        page_var.challenge = challenge
        self.page_variations.append(page_var)


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


if __name__ == "__main__":
    game = Game([4, 6])
    story = game.story
    players = game.players

    story.add_blank('00', ['apples', 'bananas', 'tomatoes'])
    story.add_blank_random('01', 'noun')
    story.add_blank_random('02', 'verb')

    story.get_page(character='alien', chapter=0, page=0).add_page_variation(
        txt=['Hello',
             'The word: ~B00~ has been randomly selected from a list',
             'And this word: ~B01~ has been randomly selected from the internet',
             'And this one as well: ~B02~',
             ]
    )

    # Adding Page 2
    story.get_page(character='alien', chapter=0, page=1).add_page_variation(
        txt=['CHALLENGE 1']
    )
    story.get_page(character='alien', chapter=0, page=1).add_page_variation(
        txt=['CHALLENGE 2']
    )

    # Adding Page 3
    story.get_page(character='alien', chapter=0, page=2).add_page_variation(
        txt=['Bad outcome']
    )
    story.get_page(character='alien', chapter=0, page=2).add_page_variation(
        txt=['Good outcome']
    )

    game.add_player('0', 'Carlos III', '')
    game.get_player('0').set_character('alien')

    # print(game.get_player(0).get_story_location())

    pv = game.get_next_page_variation('0', '')
    print(pv.txt)

    pv = game.get_next_page_variation('0', '')
    print(pv.txt)

    pv = game.get_next_page_variation('0', '')
    print(pv.txt)
