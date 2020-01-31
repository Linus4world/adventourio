import random


# --------------- ASSIGN CHARACTER ---------------

# TODO, AGATA
# Called by: game.py, line 70
def assign_characters(players):
    """"
    Parameters:
        players (dict): A dictionary, where the player_id is the key

    Returns:
        character_assignment (array of tuples):
            with the format: [(player_id, character_name), (player_id, character_name), ...]
    """
    character_assignment = []

    # --------------- YOUR CODE HERE! ---------------

    # -----------------------------------------------

    return character_assignment


def assign_characters_dummy(players):
    # ---------------  EXAMPLE: GET PLAYER ANSWERS ---------------
    answers = []
    for player_id in players.keys():
        player = players[player_id]
        player_answers = player.answers
        answers.append(player_answers)

    # ---------------  EXAMPLE: Convert player dictionary to a list ---------------
    player_list = players.values()

    # ---------------  EXAMPLE: Creating the array of tuples ---------------

    character_assignment = []
    possible_characters = ['alien', 'adventurer', 'wizard', 'detective']
    for player_id, character_name in zip(players.keys(), possible_characters):
        char_assign = (player_id, character_name)
        character_assignment.append(char_assign)

    return character_assignment


def assign_characters_dummy_2(players):
    character_assignment = random.shuffle([('01', 'alien'), ('02', 'adventurer'), ('03', 'wizard'), ('04', 'detective')])
    return character_assignment


# --------------- SELECT A CHALLENGE ---------------


# TODO, AGATA
# Called by: game.py, line 142
def select_a_challenge(players, page_variations):
    """"
    Parameters:
        players (dict): A dictionary, where the player_id is the key
        page_variations (Array of PageVariation)

    Returns:
        ret_page_variation (PageVariation): One of the page variations in the page_variations array
    """
    # EXAMPLE: Get a list of the challenges:
    challenges = []
    for page_variation_id in page_variations.keys():
        page_variation = page_variations[page_variation_id]
        challenge = page_variation.challenge
        challenges.append(challenge)

    ret_page_variation = random.choice(page_variations)  # Example of the correct dara type you have to return
    return ret_page_variation


def select_a_challenge_dummy(players, page_variations):
    return random.choice(page_variations)
