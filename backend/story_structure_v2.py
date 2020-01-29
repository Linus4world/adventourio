import numpy as np
import time
import random
from utils import *

available_characters = ['alien', 'zombie', 'wizard', 'teacher']


class CharacterError(Exception):
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
    def assign_character(self):
        # ----- YOUR CODE GOES HERE: -----
        character = random.choice()
        # ----------
        self.set_character(character)

    def set_character(self, character):
        if character in available_characters:
            self.character = character
            self.story_location[0] = available_characters.index(character)
        else:
            raise CharacterError('The character ' + character + ' does not exist!')

    def set_story_location(self, story_location):
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
        player = self.get_player(player_id)
        story_location = player.get_story_location()
        row = story_location[0]
        column = story_location[1]
        page = self.story.get_page1(row, column + 1)  # Get the next page

        # TODO: AGATA / SARAH ?
        # ----- YOUR CODE GOES HERE: -----
        page_variation = random.choice(page.page_variations) # This is a dummy functionality to return the next page variation!
        # -----

        # Filling in the blanks
        page_variation.txt = self.story.fill_in_the_blanks(page_variation)

        player.set_story_location([row, column + 1])  # Set the new location
        return page_variation


class Story:
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

    def add_challenge(self):
        pass

    def add_blank(self, blank_key, list_of_words, changes_every_time=False):
        blank = dict(
            random_word=False,
            list_of_words=list_of_words,
            keep_initial_word=changes_every_time
        )
        self.blanks['B' + blank_key] = blank

    def add_blank_random(self, blank_key, part_of_speech, changes_every_time=False):
        blank = dict(
            random_word=True,
            part_of_speech=part_of_speech,
            keep_initial_word=changes_every_time
        )
        self.blanks['B' + blank_key] = blank

    # Fill in ONE blank
    def get_the_word_for_the_blank(self, blank_key):
        blank = self.blanks[blank_key]
        # Random word from the internet!
        if blank['random_word']:
            # TODO: RANIA/SOMEONE: Improve this function to get more meaningful words!
            # It could be anything: famous people, car models, colors, a place in the world,
            # this is very very very very very very very important so
            # that the story is entertaining and most importantly CREATIVE
            part_of_speech = blank['part_of_speech']
            word = get_random_word_from_the_internet(part_of_speech)
        # Random word from the list of words provided
        else:
            list_of_words = self.blanks[blank_key]['list_of_words']
            word = random.choice(list_of_words)
        return word

    # Fill in the blank of a whole page variation
    def fill_in_the_blanks(self, page_variation):
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

    def get_page1(self, row, column):
        return self.pages[row][column]

    def get_page(self, character, chapter, page):
        row = character
        column = chapter * 3 + page
        return self.pages[row][column]


class Page:
    def __init__(self):
        self.page_name = ''
        self.page_variations = []

    def add_page_variation(self, txt=None, challenge=None):
        pv = PageVariation()
        pv.txt = txt
        self.page_variations.append(pv)


class PageVariation:
    def __init__(self):
        self.challenge = {}
        self.txt = []  # This is an array of strings
        self.story_location = (0, 0, 0)
        self.end_of_story = False


if __name__ == "__main__":

    game = Game([4, 6])
    story = game.story
    players = game.players

    story.add_blank('00', ['apples', 'bananas', 'tomatoes'])
    story.add_blank_random('01', 'noun')
    story.add_blank_random('02', 'verb')

    story.get_page(character=0, chapter=0, page=0).add_page_variation(
        txt=['Hello',
             'The word: ~B00~ has been randomly selected from a list',
             'And this word: ~B01~ has been randomly selected from the internet',
             'And this one as well: ~B02~',
             ]
    )

    # Adding Page 2
    story.get_page(character=0, chapter=0, page=1).add_page_variation(
        txt=['CHALLENGE 1']
    )
    story.get_page(character=0, chapter=0, page=1).add_page_variation(
        txt=['CHALLENGE 2']
    )

    # Adding Page 3
    story.get_page(character=0, chapter=0, page=2).add_page_variation(
        txt=['Bad outcome']
    )
    story.get_page(character=0, chapter=0, page=2).add_page_variation(
        txt=['Good outcome']
    )

    game.add_player(0, 'Carlos III', '')
    game.get_player(0).set_character('alien')

    # print(game.get_player(0).get_story_location())

    pv = game.get_next_page_variation(0, '')
    print(pv.txt)

    pv = game.get_next_page_variation(0, '')
    print(pv.txt)

    pv = game.get_next_page_variation(0, '')
    print(pv.txt)


