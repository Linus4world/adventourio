from story_structure_v2 import *
import time
from assign_characters import get_character_assignment
from all_answers_fcn import placesCategory
from challenge_assignment import new_place
from mocks_and_dummies import *
from all_answers_fcn import *


class PlayerError(Exception):
    pass


class Player:

    def __init__(self):
        self.name = ''
        self.player_id = ''
        self.challenge_outcomes = []
        self.prob_array = [(0, "good")]
        self.character = None
        self.story_location = [-1, -1]  # row, column
        self.chapter = -1
        self.geo_location = [0.0, 0.0]  # [latt, long]
        self.geo_destination = [0.0, 0.0]  # [latt, long]
        self.answers = None
        self.game_finished = False

    def set_character(self, character):
        """
        Sets the player's character and the story_location.
        The story_location[row] is the index of the character in the available_characters list.

        Parameters:
            character (Character):
                will be raised
        """
        self.character = character

    def get_character_name(self):
        return self.character.name

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

    def get_geo_location(self):
        return self.geo_location

    def get_geo_destination(self):
        return self.geo_destination

    def get_chapter_number(self):
        return (self.story_location[0] - 1)/3


class Game:
    MAX_WAIT = 50000

    def __init__(self, number_of_players, number_of_pages, number_of_dummy_players=0):
        self.story = Story([number_of_players+number_of_dummy_players, number_of_pages])
        self.fixed_character_assignment = False

        self.number_of_players = number_of_players
        self.number_of_dummy_players = number_of_dummy_players
        self.players_waiting = 0
        self.players = {}
        self.current_amount_of_players_in_game = 0
        self.current_chapter = 0

        self.ready_queue = 0
        self.ready_to_play = False
        self.finished_game = False
        self.places_category = dict()
        self.player_characters = dict()
        self.player_challenge_outcome = dict()
        self.player_next_chapter = dict()

        # ------------------ HANDLE MOCK PLAYERS: -------------------
        # Add Player
        for i in range(number_of_dummy_players):
            player_input = {
                "name": 'Player'+str(i),
                "answers": [
                    "Entertainment","yes","yes","Adventure/action","To experience other cultures","Deutsches Museum","mostly friends from the university"
                    ]
                }
            self.add_player(str(i), player_input)
            player = self.get_player(str(i))
            player.challenge_outcomes.append(True)
            print('[MOCK]: added player', player.name)

    # --------------- SET UP: ---------------

    def start_game(self):
        """
        This function does all the set up, before the game gets started:
            - Assign characters

        Parameters: None
        Returns: None
        """

        # Package all the player answers into one object:
        all_player_answers = all_answers_function_v2(self.players)
        with open("challenges.json", 'r', encoding='utf-8') as file:
            challenges = file.read()

        # CHARACTER ASSIGNMENT
        character_assignment = get_character_assignment(all_player_answers)
        # character_assignment = assign_characters_dummy(self.players)

        for player_id in character_assignment.keys():
            # Set character for each player
            player = self.get_player(player_id)
            character_name = character_assignment[player_id]
            character = self.story.get_character(character_name=character_name)
            player.set_character(character)
            # Set player's story location (row)
            player.story_location[0] = self.story.get_character_story_row(character_name=character_name)

        # Set places category
        self.set_place_category(placesCategory(answers2, challenges))
        self.ready_to_play = True

    # --------------- MANAGING PLAYERS: ---------------
    def add_player(self, player_id, player_input):
        if player_id in self.players.keys():
            raise PlayerError('This player id is already reserved!')

        new_player = Player()
        new_player.name = player_input['name']
        new_player.player_id = player_id
        new_player.answers = player_input['answers']
        self.players[player_id] = new_player

    def get_player_id_with_character_name(self, character_name):
        for player_id in self.players.keys():
            if self.players[player_id].character.name == character_name:
                return player_id

    def is_full(self):
        return len(self.players) >= self.number_of_players + self.number_of_dummy_players

    def is_game_ready(self):
        return self.ready_queue >= self.number_of_players-1

    def get_player_count(self):
        return len(self.players)

    def get_player_names(self):
        player_names = []
        for player in self.players.values():
            player_names.append(player.name)
        return player_names

    # def get_player_index(self, player_id):
    #     return self.playerIds.index(player_id)

    def get_player(self, player_id):
        return self.players[player_id]

    def wait_for_game_ready(self):
        self.ready_queue += 1
        counter = 0
        while counter < self.MAX_WAIT:
            if self.ready_to_play:
                self.leave_game()
                return True
            time.sleep(2)
            counter += 1
        return False

    def leave_game(self):
        self.ready_queue -= 1
        if self.ready_queue <= 0:
            self.ready_to_play = False
            print('Blocked')

    # --------------- X: ---------------

    def set_place_category(self, places_category):
        self.places_category = places_category

    def get_place_category(self):
        return self.places_category

    def get_current_chapter(self):
        return self.current_chapter

    # --------------- STORY LOGIC: ---------------

    def get_next_page_variation(self, player_id, challenge_outcome):
        """
        This function will be constantly called by the frontend to get the next page variation
        Depending on the player, the player.story_location and player_input, the next page variation can be selected

        Parameters:
            player_id (str):
            challenge_outcome (bool):

        Returns:
            PageVariation:
        """
        story = self.story
        player = self.get_player(player_id)

        # Get the next page
        story_location = player.get_story_location()
        row = story_location[0]
        column = story_location[1]

        # Set the new location
        player.set_story_location([row, column + 1])

        page = self.story.get_page_raw(row, column + 1)
        if page.is_it_the_last_page():
            player.game_finished = True

        page_variation = PageVariation()

        if page.page_variations:
            # If the page is a challenge page:
            if page.page_type == 'challenge':
                page_variation.challenge = dict()
            # If the page is an outcome page:
            elif page.page_type == 'outcome':
                assert len(page.page_variations) == 2, str(len(page.page_variations))
                page_variation = story.select_good_or_bad_outcome(page.page_variations, player)
            # IF IT IS NOT SPECIFIED WHAT TYPE OF PAGE THIS IS, A RANDOM PAGE VARIATION WILL BE SELECTED!
            else:
                page_variation = random.choice(page.page_variations)

            # Filling in the blanks
            page_variation.txt = story.fill_in_the_blanks(page_variation)

        return page_variation

    def get_next_story_section(self, player_id, challenge_outcome):
        story_text = []

        # Story player input
        player = self.get_player(player_id)
        player.challenge_outcomes.append(challenge_outcome)

        challenge_found = False
        game_finished = self.players[player_id].game_finished
        while not challenge_found and not game_finished:
            page_variation = self.get_next_page_variation(player_id, challenge_outcome)

            # This has to be called AFTER get_next_page_variation
            game_finished = self.players[player_id].game_finished

            if page_variation.txt != '':
                story_text.extend(page_variation.txt)
            if page_variation.challenge is not None:
                challenge_found = True

        ret_dict = dict(
            story=story_text,
            game_finished=game_finished,
        )

        return ret_dict
