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
        self.player_inputs = []
        self.prob_array = [(0, "good")]
        self.character = ''
        self.story_location = [-1, -1]  # row, column
        self.geo_location = [0.0, 0.0]  # [latt, long]
        self.geo_destination = [0.0, 0.0]  # [latt, long]
        self.answer = None
        self.game_finished = False

    # TODO: AGATA / SARAH
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

    def __init__(self, number_of_players, number_of_pages):
        self.story = Story([number_of_players, number_of_pages])
        self.max_players = number_of_players
        self.players = []

    def add_player(self, player_id, name, answer):
        player = Player()
        player.name = name
        player.player_id = player_id
        player.answer = answer
        self.players.append(player)

    def is_full(self):
        return len(self.players) >= self.max_players

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

        # Story player input
        player.player_inputs.append(player_input)

        # Get the next page
        story_location = player.get_story_location()
        row = story_location[0]
        column = story_location[1]
        page = self.story.get_page_raw(row, column + 1)

        page_variation = PageVariation()
        # If there is only one page variation, return that one
        if len(page.page_variations) == 1:
            page_variation = page.page_variations[0]
        # If the page is a challenge page:
        elif page.page_type == 'challenges':
            # TODO: Replace this with AGATA'S CHALLENGE SELECTING FUNCTION
            page_variation = story.select_page_variation_dummy(page.page_variations, player)
        # If the page is an outcome page:
        elif page.page_type == 'outcome':
            page_variation = story.select_good_or_bad_outcome(page.page_variations, player)
        # IF IT IS NOT SPECIFIED WHAT TYPE OF PAGE THIS IS, A RANDOM PAGE VARIATION WILL BE SELECTED!
        else:
            page_variation = random.choice(page.page_variations)

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

    def setup_story(self):
        pass

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

    @staticmethod
    def select_page_variation_dummy(page_variations, player):
        return random.choice(page_variations)  # DUMMY FUNCTION!

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


if __name__ == "__main__":
    game = Game(number_of_players=4, number_of_pages=6)
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
    # story.get_page(character='alien', chapter=0, page=1).set_page_type('challenge')
    story.get_page(character='alien', chapter=0, page=1).add_page_variation(
        txt=['CHALLENGE 1']
    )
    story.get_page(character='alien', chapter=0, page=1).add_page_variation(
        txt=['CHALLENGE 2']
    )

    # Adding Page 3
    story.get_page(character='alien', chapter=0, page=2).set_page_type('outcome')
    story.get_page(character='alien', chapter=0, page=2).add_page_variation(
        txt=['Good outcome']
    )
    story.get_page(character='alien', chapter=0, page=2).add_page_variation(
        txt=['Bad outcome']
    )

    game.add_player('0', 'Carlos III', '')
    game.get_player('0').set_character('alien')

    # print(game.get_player(0).get_story_location())

    # The next few lines simulate what we would get from the front end
    pv = game.get_next_page_variation('0', player_input=True)
    print(pv.txt)

    pv = game.get_next_page_variation('0', player_input=True)
    print(pv.txt)

    pv = game.get_next_page_variation('0', player_input=True)
    print(pv.txt)
