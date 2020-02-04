import random
import json


def assign_characters_dummy(players):
    character_assignment = {}
    random.seed()
    possible_characters = ['alien', 'adventurer', 'wizard', 'detective']
    # random.shuffle(possible_characters)  # COMMENT FOR TESTING!
    for player_id, character_name in zip(players.keys(), possible_characters):
        character_assignment[player_id] = character_name
    return character_assignment


def get_a_challenge_dummy(players):
    with open('challenges_v2.json', 'r', encoding='utf-8') as json_file:
        challenges = json.load(json_file)
    random.seed()
    challenges = list(challenges.values())
    return random.choice(challenges)


# Mock json for testing the character assignment
answers1 = """
{
    "all_answers": [
        {
            "id": "00",
            "answers": [
                "a",
                "a",
                "d",
                "d"
            ]
        },
        {
            "id": "01",
            "answers": [
                "a",
                "b",
                "b",
                "c"
            ]
        },
        {
            "id": "02",
            "answers": [
                "b",
                "c",
                "a",
                "a"
            ]
        },
        {
            "id": "03",
            "answers": [
                "b",
                "c",
                "b",
                "b"
            ]
        }          
    ]
}
"""
answers2 = """
{
    "all_answers": [
        {
            "id": "89",
            "name": "ja",
            "answers": [
                "a",
                "a",
                "a",
                "d",
                "c",
                "d",
                "b"
            ]
        },
        {
            "id": "2",
            "name": "ja2",
            "answers": [
                "a",
                "a",
                "a",
                "d",
                "c",
                "d",
                "b"
            ]
        },
        {
            "id": "3",
            "name": "ja3",
            "answers": [
                "a",
                "a",
                "a",
                "a",
                "b",
                "b",
                "c"
            ]
        },
        {
            "id": "4",
            "name": "ja4",
            "answers": [
                "a",
                "a",
                "a",
                "b",
                "c",
                "b",
                "b"
            ]
        }          
    ]
}
"""
answers3 = """
{
    "all_answers": [
        {
            "id": "1",
            "name": "ja",
            "answers": [
                "a",
                "a",
                "a",
                "a",
                "b",
                "c",
                "d"
            ]
        },
        {
            "id": "2",
            "name": "ja2",
            "answers": [
                "a",
                "a",
                "a",
                "a",
                "b",
                "c",
                "d"
            ]
        },
        {
            "id": "3",
            "name": "ja3",
            "answers": [
                "a",
                "a",
                "a",
                "c",
                "a",
                "c",
                "d"
            ]
        },
        {
            "id": "4",
            "name": "ja4",
            "answers": [
                "a",
                "a",
                "a",
                "d",
                "b",
                "b",
                "c"
            ]
        }          
    ]
}
"""