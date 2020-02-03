from story_structure_v2 import *
from characters_and_challenges import *


class PlayerError(Exception):
    pass


class Player:

    def __init__(self):
        self.name = ''
        self.player_id = ''
        self.player_inputs = []
        self.prob_array = [(0, "good")]
        self.character = None
        self.story_location = [-1, -1]  # row, column
        self.chapter = -1
        self.geo_location = [0.0, 0.0]  # [latt, long]
        self.geo_destination = [0.0, 0.0]  # [latt, long]
        self.answer = None
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
        self.story_location[0] = story.get_character_story_row(character_name=character.name)

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
        self.max_players = number_of_players
        self.players = {}

    # --------------- SET UP: ---------------

    def start_game(self):
        """
        This function does all the set up, before the game gets started:
            - Assign characters

        Parameters: None
        Returns: None
        """
        assert self.is_full(), 'Can\'t start the game if it is not full!'

        # Assign the characters
        character_assignments = assign_characters_dummy(self.players)
        for char_assign in character_assignments:
            player_id = char_assign[0]
            player = self.get_player(player_id)

            character_name = char_assign[1]
            character = self.story.get_character(character_name)

            player.set_character(character)

    def setPlacesCategory(self, places):
        self.placesCategory = places

    def getPlacesCategory(self):
        return self.placesCategory

    # --------------- MANAGING PLAYERS: ---------------

    def add_player(self, player_id, name, answers):
        new_player = Player()
        new_player.name = name
        new_player.player_id = player_id
        new_player.answers = answers
        self.players[player_id] = new_player

    def is_full(self):
        return len(self.players) >= self.max_players

    # def get_player_index(self, player_id):
    #     return self.playerIds.index(player_id)

    def get_player(self, player_id):
        return self.players[player_id]

    # --------------- X: ---------------

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
            page_variation = select_a_challenge_dummy(page.page_variations, self.players)
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


if __name__ == "__main__":
    game = Game(number_of_players=4, number_of_pages=6)

    story = game.story
    story.setup_story()

    game.add_player(player_id='01', name='Carlos I', answers='')
    game.add_player(player_id='02', name='Carlos I', answers='')
    game.add_player(player_id='03', name='Carlos III', answers='')
    game.add_player(player_id='04', name='Carlos IV', answers='')

    game.start_game()
    players = game.players

    for player in players.values():
        print(player.character.name)

    # Add blanks to the story:
    story.add_blank('B00', ['apples', 'bananas', 'tomatoes'], changes_every_time=True)
    story.add_blank_random('B01', 'noun')
    story.add_blank_random('B02', 'verb')

    # Add challenges to the story:
    story.load_all_challenges('challenges_v2.json')

    # # Add content of the story:
    story.get_page(character_name='alien', chapter=0, page=0).add_page_variation(
        txt=['Hello',
             'The word: ~B00~ has been randomly selected from a list',
             'And this word: ~B01~ has been randomly selected from the internet',
             'And this one as well: ~B02~',
             ]
    )

    # Adding Page 2
    # story.get_page(character='alien', chapter=0, page=1).set_page_type('challenge')
    story.get_page(character_name='alien', chapter=0, page=1).add_page_variation(
        txt=['CHALLENGE 1'], challenge=story.get_challenge('00')
    )
    story.get_page(character_name='alien', chapter=0, page=1).add_page_variation(
        txt=['CHALLENGE 2'], challenge=story.get_challenge('01')
    )

    # Adding Page 3
    story.get_page(character_name='alien', chapter=0, page=2).set_page_type('outcome')
    story.get_page(character_name='alien', chapter=0, page=2).add_page_variation(
        txt=['Good outcome']
    )
    story.get_page(character_name='alien', chapter=0, page=2).add_page_variation(
        txt=['Bad outcome']
    )


    # The next few lines simulate what we would get from the front end
    pv = game.get_next_page_variation(player_id='01', player_input=True)
    print(pv.txt)

    pv = game.get_next_page_variation(player_id='01', player_input=True)
    print(pv.txt)

    pv = game.get_next_page_variation(player_id='01', player_input=True)
    print(pv.txt)
