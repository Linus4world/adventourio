import numpy as np
import time


class Player:
    def __init__(self):
        self.name = ''
        self.player_id = ''
        self.story_location = (-1, -1, -1)
        self.geo_location = []
        self.answer = None
        self.game_finished = False


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

    def wait_for_full_session(self):
        counter = 0
        while counter < self.MAX_WAIT:
            if self.is_full():
                return True
            time.sleep(2)
            counter += 1
        return False

    def get_next_stage_variation(self, player_id, player_input):
        pass


class Story:
    def __init__(self, story_size):
        self.sub_stages = np.zeros((story_size[0], story_size[1]), dtype=StageVariation)
        self.challenges = []
        self.blanks = []

    def add_challenge(self):
        pass

    def add_blank(self):
        pass

    def add_blank_random(self):
        pass

    def add_stage_variation(self):
        pass

    def get_stage_variation(self, character, stage, sub_stage):
        pass


class StageVariation:
    def __init__(self):
        self.challenge = {}
        self.txt = []  # This is an array of strings
        self.story_location = (0, 0, 0)
        self.end_of_story = False


if __name__ == "__main__":
    pass

