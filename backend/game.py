from story_structure_v2 import *
import time
from assign_characters import get_character_assignment
from challenge_assignment import new_place
from mocks_and_dummies import *


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

    def __init__(self, number_of_players, number_of_pages):
        self.story = Story([number_of_players, number_of_pages])
        self.number_of_players = number_of_players
        self.players_waiting = 0
        self.players = {}
        self.current_amount_of_players_in_game = 0

        self.ready_queue = 0
        self.ready_to_play = False
        self.finished_game = False
        self.places_category = dict()
        self.player_characters = dict()
        self.player_challenge_outcome = dict()
        self.player_next_chapter = dict()

    # --------------- SET UP: ---------------

    def start_game(self, all_answers, challenges):
        """
        This function does all the set up, before the game gets started:
            - Assign characters

        Parameters: None
        Returns: None
        """
        # Assign the characters
        character_assignment = assign_characters_dummy(self.players)  # TODO: REPLACE WITH AGATA'S FUNCTION
        # character_assignment = get_character_assignment(all_answers)

        for player_id in character_assignment.keys():
            # Set character for each player
            player = self.get_player(player_id)
            character_name = character_assignment[player_id]
            character = self.story.get_character(character_name=character_name)
            player.set_character(character)
            # Set player's story location (row)
            player.story_location[0] = self.story.get_character_story_row(character_name=character_name)

        # Set places category
        self.set_place_category(challenges)

    # --------------- MANAGING PLAYERS: ---------------
    def add_player(self, player_id, answers):
        if player_id in self.players.keys():
            raise PlayerError('This player id is already reserved!')

        new_player = Player()
        new_player.name = answers['name']
        new_player.player_id = player_id
        new_player.answers = answers['answers']
        self.players[player_id] = new_player

    def is_full(self):
        return len(self.players) >= self.number_of_players

    def get_player_count(self):
        return len(self.players)

    # def get_player_index(self, player_id):
    #     return self.playerIds.index(player_id)

    def get_player(self, player_id):
        return self.players[player_id]

    def wait_for_session_ready(self):
        self.players_waiting += 1
        counter = 0
        while counter < self.MAX_WAIT:
            if self.ready_to_play:
                # self.leave()
                return True
            time.sleep(2)
            counter += 1
        return False

    # def leave(self):
    #     self.readyQueue -= 1
    #     if self.readyQueue == 0:
    #         self.ready_to_play = False

    # --------------- X: ---------------

    def set_place_category(self, places_category):
        self.places_category = places_category

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

        # Story player input
        player.challenge_outcomes.append(challenge_outcome)

        # Get the next page
        story_location = player.get_story_location()
        row = story_location[0]
        column = story_location[1]

        # Set the new location
        player.set_story_location([row, column + 1])

        page = self.story.get_page_raw(row, column + 1)
        if page.is_it_the_last_page():
            player.game_finished = True

        # If there is only one page variation, return that one
        if len(page.page_variations) == 1:
            page_variation = page.page_variations[0]
        # If the page is a challenge page:
        elif page.page_type == 'challenge':
            # Create a page_variation on the fly:
            page_variation = PageVariation()
            challenge = get_a_challenge_dummy(self.players)  # TODO: REPLACE WITH AGATA'S FUNCTION
            # challenge = new_place(self)
            page_variation.challenge = challenge
        # If the page is an outcome page:
        elif page.page_type == 'outcome':
            page_variation = story.select_good_or_bad_outcome(page.page_variations, player)
        # IF IT IS NOT SPECIFIED WHAT TYPE OF PAGE THIS IS, A RANDOM PAGE VARIATION WILL BE SELECTED!
        else:
            page_variation = random.choice(page.page_variations)

        # Filling in the blanks
        page_variation.txt = story.fill_in_the_blanks(page_variation)

        return page_variation

    def get_next_story_section(self, player_id, challenge_outcome):
        txt = []
        challenge = {}

        challenge_found = False
        game_finished = self.players[player_id].game_finished
        while not challenge_found and not game_finished:
            page_variation = self.get_next_page_variation(player_id, challenge_outcome)

            # This has to be called AFTER get_next_page_variation
            game_finished = self.players[player_id].game_finished

            if page_variation.txt != '':
                txt += page_variation.txt
            if page_variation.challenge is not None:
                challenge_found = True
                challenge = page_variation.challenge

        ret_dict = dict(txt=txt, challenge=challenge)

        return ret_dict
        # return json.dumps(ret_dict)
