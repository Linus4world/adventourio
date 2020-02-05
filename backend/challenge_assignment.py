import math

"""
class Player:
    # destination - the places of the current stage, player assumed to be there
    # stage - current stage in the story
    def __init__(self, destination, stage):
        self.destination = destination
        self.stage = stage


def select_a_challenge(page_variations, player):
    pass

"""

def getCharacterId(character, game):
    if game["characters"][0].name == character:
        return 0
    elif game["characters"][1].name == character:
        return 1
    elif game["characters"][2].name == character:
        return 2
    elif game["characters"][3].name == character:
        return 3


def new_place(game):
    """
    alien = ['Adventurer', 'Wizard', 'Detective']
    adventurer = ['Alien', 'Detective', 'Wizard']
    detective = ['Wizard', 'Adventurer', 'Alien']
    wizard = ['Detective', 'Alien', 'Adventurer']
    """

    # ORIGINAL CODE (agata)
    # alien_id = getCharacterId("alien", game)
    # adventurer_id = getCharacterId("adventurer", game)
    # detective_id = getCharacterId("detective", game)
    # wizard_id = getCharacterId("wizard", game)

    # NEW CODE (ESTEBAN)
    alien_id = game.get_player_id_with_character_name('alien')
    adventurer_id = game.get_player_id_with_character_name('adventurer')
    detective_id = game.get_player_id_with_character_name('detective')
    wizard_id = game.get_player_id_with_character_name('wizard')

    places_in = game.get_place_category()
    stage = game.get_current_chapter() + 1
    one_json = {}
    print('stage: ', stage)

    if stage == 1:

        # OLD
        # destination1 = game["characters"][alien_id].geo_location
        # destination2 = game["characters"][adventurer_id].geo_location

        # NEW
        destination1 = game.players[alien_id].geo_location
        destination2 = game.players[adventurer_id].geo_location

        # calculate middle point between two players
        if destination1[0] >= destination2[0]:
            new_latt = destination1[0] - (destination1[0] - destination2[0]) / 2
        else:
            new_latt = destination2[0] - (destination2[0] - destination1[0]) / 2

        if destination1[1] >= destination2[1]:
            new_long = destination1[1] - (destination1[1] - destination2[1]) / 2
        else:
            new_long = destination2[1] - (destination2[1] - destination1[1]) / 2

        r_old = 0
        destinationCoords = [0, 0]
        destinationName = 0
        challenge = "null"
        challenge_type = 0
        options = []
        right_answer = []
        for stages in places_in['stages']:
            if stages['stage'] == stage:
                for place in stages['places']:
                    r1 = math.pow(place['coordinates'][0] - new_latt, 2)
                    r2 = math.pow(place['coordinates'][1] - new_long, 2)
                    r = math.sqrt(r1 + r2)
                    if r < r_old or r_old == 0:
                        destinationName = place['title']
                        destinationCoords[0] = place['coordinates'][0]
                        destinationCoords[1] = place['coordinates'][1]
                        challenge = place['challenge']
                        challenge_type = place['challenge_type']
                        if challenge_type == 1:
                            options = place['options']
                        right_answer = place['right_answer']
                        r_old = r

        # OLD:
        # destination1 = game["characters"][wizard_id].geo_location
        # destination2 = game["characters"][alien_id].geo_location

        # NEW:
        destination1 = game.players[wizard_id].geo_location
        destination2 = game.players[alien_id].geo_location

        # calculate middle point between two players
        if destination1[0] >= destination2[0]:
            new_latt = destination1[0] - (destination1[0] - destination2[0]) / 2
        else:
            new_latt = destination2[0] - (destination2[0] - destination1[0]) / 2

        if destination1[1] >= destination2[1]:
            new_long = destination1[1] - (destination1[1] - destination2[1]) / 2
        else:
            new_long = destination2[1] - (destination2[1] - destination1[1]) / 2

        r_old = 0
        destinationCoords1 = [0, 0]
        destinationName1 = 0
        challenge1 = "null"
        challenge_type1 = 0
        options1 = []
        right_answer1 = []
        for stages in places_in['stages']:
            if stages['stage'] == stage:
                for place in stages['places']:
                    r1 = math.pow(place['coordinates'][0] - new_latt, 2)
                    r2 = math.pow(place['coordinates'][1] - new_long, 2)
                    r = math.sqrt(r1 + r2)
                    if (r < r_old or r_old == 0) and place['title'] != destinationName:
                        destinationName1 = place['title']
                        destinationCoords1[0] = place['coordinates'][0]
                        destinationCoords1[1] = place['coordinates'][1]
                        challenge1 = place['challenge']
                        challenge_type1 = place['challenge_type']
                        if challenge_type1 == 1:
                            options1 = place['options']
                        right_answer1 = place['right_answer']
                        r_old = r
        if challenge_type == 1:
            one_json[alien_id] = {'destinationName': destinationName, 'destinationCoords': destinationCoords,
                                     'challenge': {'challenge': challenge, 'challenge_type': challenge_type,
                                                   'right_answer': right_answer, 'options': options}}
            one_json[adventurer_id] = {'destinationName': destinationName, 'destinationCoords': destinationCoords,
                                          'challenge': {'challenge': challenge, 'challenge_type': challenge_type,
                                                        'right_answer': right_answer, 'options': options}}
        else:
            one_json[alien_id] = {'destinationName': destinationName, 'destinationCoords': destinationCoords,
                                     'challenge': {'challenge': challenge, 'challenge_type': challenge_type,
                                                   'right_answer': right_answer}}
            one_json[adventurer_id] = {'destinationName': destinationName, 'destinationCoords': destinationCoords,
                                          'challenge': {'challenge': challenge, 'challenge_type': challenge_type,
                                                        'right_answer': right_answer}}
        if challenge_type1 == 1:
            one_json[wizard_id] = {'destinationName': destinationName1, 'destinationCoords': destinationCoords1,
                                      'challenge': {'challenge': challenge1, 'challenge_type': challenge_type1,
                                                    'right_answer': right_answer1, 'options': options1}}
            one_json[detective_id] = {'destinationName': destinationName1, 'destinationCoords': destinationCoords1,
                                     'challenge': {'challenge': challenge1, 'challenge_type': challenge_type1,
                                                   'right_answer': right_answer1, 'options': options1}}
        else:
            one_json[wizard_id] = {'destinationName': destinationName1, 'destinationCoords': destinationCoords1,
                                      'challenge': {'challenge': challenge1, 'challenge_type': challenge_type1,
                                                    'right_answer': right_answer1}}
            one_json[detective_id] = {'destinationName': destinationName1, 'destinationCoords': destinationCoords1,
                                     'challenge': {'challenge': challenge1, 'challenge_type': challenge_type1,
                                                   'right_answer': right_answer1}}
        return one_json

    elif stage == 2:
        # destination1 = game["characters"][detective_id].geo_location
        # destination2 = game["characters"][adventurer_id].geo_location
        destination1 = game.players[detective_id].geo_location
        destination2 = game.players[adventurer_id].geo_location
        # calculate middle point between two players
        if destination1[0] >= destination2[0]:
            new_latt = destination1[0] - (destination1[0] - destination2[0]) / 2
        else:
            new_latt = destination2[0] - (destination2[0] - destination1[0]) / 2

        if destination1[1] >= destination2[1]:
            new_long = destination1[1] - (destination1[1] - destination2[1]) / 2
        else:
            new_long = destination2[1] - (destination2[1] - destination1[1]) / 2

        r_old = 0
        destinationCoords = [0, 0]
        destinationName = 0
        challenge = "null"
        challenge_type = 0
        options = []
        right_answer = []
        for stages in places_in['stages']:
            if stages['stage'] == stage:
                for place in stages['places']:
                    r1 = math.pow(place['coordinates'][0] - new_latt, 2)
                    r2 = math.pow(place['coordinates'][1] - new_long, 2)
                    r = math.sqrt(r1 + r2)
                    if r < r_old or r_old == 0:
                        destinationName = place['title']
                        destinationCoords[0] = place['coordinates'][0]
                        destinationCoords[1] = place['coordinates'][1]
                        challenge = place['challenge']
                        challenge_type = place['challenge_type']
                        if challenge_type == 1:
                            options = place['options']
                        right_answer = place['right_answer']
                        r_old = r

        # destination1 = game["characters"][wizard_id].geo_location
        # destination2 = game["characters"][detective_id].geo_location
        destination1 = game.players[wizard_id].geo_location
        destination2 = game.players[detective_id].geo_location
        # calculate middle point between two players
        if destination1[0] >= destination2[0]:
            new_latt = destination1[0] - (destination1[0] - destination2[0]) / 2
        else:
            new_latt = destination2[0] - (destination2[0] - destination1[0]) / 2

        if destination1[1] >= destination2[1]:
            new_long = destination1[1] - (destination1[1] - destination2[1]) / 2
        else:
            new_long = destination2[1] - (destination2[1] - destination1[1]) / 2

        r_old = 0
        destinationCoords1 = [0, 0]
        destinationName1 = 0
        challenge1 = "null"
        challenge_type1 = 0
        options1 = []
        right_answer1 = []
        for stages in places_in['stages']:
            if stages['stage'] == stage:
                for place in stages['places']:
                    r1 = math.pow(place['coordinates'][0] - new_latt, 2)
                    r2 = math.pow(place['coordinates'][1] - new_long, 2)
                    r = math.sqrt(r1 + r2)
                    if (r < r_old or r_old == 0) and place['title'] != destinationName:
                        destinationName1 = place['title']
                        destinationCoords1[0] = place['coordinates'][0]
                        destinationCoords1[1] = place['coordinates'][1]
                        challenge1 = place['challenge']
                        challenge_type1 = place['challenge_type']
                        if challenge_type1 == 1:
                            options1 = place['options']
                        right_answer1 = place['right_answer']
                        r_old = r
        if challenge_type == 1:
            one_json[detective_id] = {'destinationName': destinationName, 'destinationCoords': destinationCoords,
                                       'challenge': {'challenge': challenge, 'challenge_type': challenge_type,
                                                     'right_answer': right_answer, 'options': options}}
            one_json[adventurer_id] = {'destinationName': destinationName, 'destinationCoords': destinationCoords,
                                        'challenge': {'challenge': challenge, 'challenge_type': challenge_type,
                                                      'right_answer': right_answer, 'options': options}}
        else:
            one_json[detective_id] = {'destinationName': destinationName, 'destinationCoords': destinationCoords,
                                       'challenge': {'challenge': challenge, 'challenge_type': challenge_type,
                                                     'right_answer': right_answer}}
            one_json[adventurer_id] = {'destinationName': destinationName, 'destinationCoords': destinationCoords,
                                        'challenge': {'challenge': challenge, 'challenge_type': challenge_type,
                                                      'right_answer': right_answer}}
        if challenge_type1 == 1:
            one_json[wizard_id] = {'destinationName': destinationName1, 'destinationCoords': destinationCoords1,
                        'challenge': {'challenge': challenge1, 'challenge_type': challenge_type1,
                                        'right_answer': right_answer1, 'options': options1}}
            one_json[alien_id] = {'destinationName': destinationName1, 'destinationCoords': destinationCoords1,
                        'challenge': {'challenge': challenge1, 'challenge_type': challenge_type1,
                                        'right_answer': right_answer1, 'options': options1}}
        else:
            one_json[wizard_id] = {'destinationName': destinationName1, 'destinationCoords': destinationCoords1,
                        'challenge': {'challenge': challenge1, 'challenge_type': challenge_type1,
                                        'right_answer': right_answer1}}
            one_json[alien_id] = {'destinationName': destinationName1, 'destinationCoords': destinationCoords1,
                        'challenge': {'challenge': challenge1, 'challenge_type': challenge_type1,
                                        'right_answer': right_answer1}}
        return one_json

    elif stage == 3:

        # destination1 = game["characters"][detective_id].geo_location
        # destination2 = game["characters"][alien_id].geo_location
        destination1 = game.players[detective_id].geo_location
        destination2 = game.players[alien_id].geo_location

        # calculate middle point between two players
        if destination1[0] >= destination2[0]:
            new_latt = destination1[0] - (destination1[0] - destination2[0]) / 2
        else:
            new_latt = destination2[0] - (destination2[0] - destination1[0]) / 2

        if destination1[1] >= destination2[1]:
            new_long = destination1[1] - (destination1[1] - destination2[1]) / 2
        else:
            new_long = destination2[1] - (destination2[1] - destination1[1]) / 2

        r_old = 0
        destinationCoords = [0, 0]
        destinationName = 0
        challenge = "null"
        challenge_type = 0
        options = []
        right_answer = []
        for stages in places_in['stages']:
            if stages['stage'] == stage:
                for place in stages['places']:
                    r1 = math.pow(place['coordinates'][0] - new_latt, 2)
                    r2 = math.pow(place['coordinates'][1] - new_long, 2)
                    r = math.sqrt(r1 + r2)
                    if r < r_old or r_old == 0:
                        destinationName = place['title']
                        destinationCoords[0] = place['coordinates'][0]
                        destinationCoords[1] = place['coordinates'][1]
                        challenge = place['challenge']
                        challenge_type = place['challenge_type']
                        if challenge_type == 1:
                            options = place['options']
                        right_answer = place['right_answer']
                        r_old = r

        # destination1 = game["characters"][wizard_id].geo_location
        # destination2 = game["characters"][adventurer_id].geo_location
        destination1 = game.players[wizard_id].geo_location
        destination2 = game.players[adventurer_id].geo_location
        # calculate middle point between two players

        if destination1[0] >= destination2[0]:
            new_latt = destination1[0] - (destination1[0] - destination2[0]) / 2
        else:
            new_latt = destination2[0] - (destination2[0] - destination1[0]) / 2

        if destination1[1] >= destination2[1]:
            new_long = destination1[1] - (destination1[1] - destination2[1]) / 2
        else:
            new_long = destination2[1] - (destination2[1] - destination1[1]) / 2

        r_old = 0
        destinationCoords1 = [0, 0]
        destinationName1 = 0
        challenge1 = "null"
        challenge_type1 = 0
        options1 = []
        right_answer1 = []
        for stages in places_in['stages']:
            if stages['stage'] == stage:
                for place in stages['places']:
                    r1 = math.pow(place['coordinates'][0] - new_latt, 2)
                    r2 = math.pow(place['coordinates'][1] - new_long, 2)
                    r = math.sqrt(r1 + r2)
                    if (r < r_old or r_old == 0) and place['title'] != destinationName:
                        destinationName1 = place['title']
                        destinationCoords1[0] = place['coordinates'][0]
                        destinationCoords1[1] = place['coordinates'][1]
                        challenge1 = place['challenge']
                        challenge_type1 = place['challenge_type']
                        if challenge_type1 == 1:
                            options1 = place['options']
                        right_answer1 = place['right_answer']
                        r_old = r

        if challenge_type == 1:
            one_json[detective_id] = {'destinationName': destinationName, 'destinationCoords': destinationCoords,
                                       'challenge': {'challenge': challenge, 'challenge_type': challenge_type,
                                                     'right_answer': right_answer, 'options': options}}
            one_json[alien_id] = {'destinationName': destinationName, 'destinationCoords': destinationCoords,
                                   'challenge': {'challenge': challenge, 'challenge_type': challenge_type,
                                                 'right_answer': right_answer, 'options': options}}
        else:
            one_json[detective_id] = {'destinationName': destinationName, 'destinationCoords': destinationCoords,
                                       'challenge': {'challenge': challenge, 'challenge_type': challenge_type,
                                                     'right_answer': right_answer}}
            one_json[alien_id] = {'destinationName': destinationName, 'destinationCoords': destinationCoords,
                                   'challenge': {'challenge': challenge, 'challenge_type': challenge_type,
                                                 'right_answer': right_answer}}
        if challenge_type1 == 1:
            one_json[wizard_id] = {'destinationName': destinationName1, 'destinationCoords': destinationCoords1,
                                    'challenge': {'challenge': challenge1, 'challenge_type': challenge_type1,
                                                  'right_answer': right_answer1, 'options': options1}}
            one_json[adventurer_id] = {'destinationName': destinationName1, 'destinationCoords': destinationCoords1,
                                        'challenge': {'challenge': challenge1, 'challenge_type': challenge_type1,
                                                      'right_answer': right_answer1, 'options': options1}}
        else:
            one_json[wizard_id] = {'destinationName': destinationName1, 'destinationCoords': destinationCoords1,
                                    'challenge': {'challenge': challenge1, 'challenge_type': challenge_type1,
                                                  'right_answer': right_answer1}}
            one_json[adventurer_id] = {'destinationName': destinationName1, 'destinationCoords': destinationCoords1,
                                        'challenge': {'challenge': challenge1, 'challenge_type': challenge_type1,
                                                      'right_answer': right_answer1}}
        return one_json

    elif stage == 4:
        destination1 = game.players[wizard_id].geo_location
        destination2 = game.players[detective_id].geo_location
        destination1 = game.players[wizard_id].geo_location
        destination2 = game.players[detective_id].geo_location

        if destination1[0] >= destination2[0]:
            new_latt = destination1[0] - (destination1[0] - destination2[0]) / 2
        else:
            new_latt = destination2[0] - (destination2[0] - destination1[0]) / 2

        if destination1[1] >= destination2[1]:
            new_long = destination1[1] - (destination1[1] - destination2[1]) / 2
        else:
            new_long = destination2[1] - (destination2[1] - destination1[1]) / 2

        r_old = 0
        destinationCoords = [0, 0]
        destinationName = 0
        challenge = "null"
        challenge_type = 0
        options = []
        right_answer = []
        for stages in places_in['stages']:
            if stages['stage'] == stage:
                for place in stages['places']:
                    r1 = math.pow(place['coordinates'][0] - new_latt, 2)
                    r2 = math.pow(place['coordinates'][1] - new_long, 2)
                    r = math.sqrt(r1 + r2)
                    if (r < r_old or r_old == 0):
                        destinationName = place['title']
                        destinationCoords[0] = place['coordinates'][0]
                        destinationCoords[1] = place['coordinates'][1]
                        challenge = place['challenge']
                        challenge_type = place['challenge_type']
                        if challenge_type == 1:
                            options = place['options']
                        right_answer = place['right_answer']
                        r_old = r

        if challenge_type == 1:
            one_json = {detective_id: {'destinationName': destinationName, 'destinationCoords': destinationCoords,
                                       'challenge': {'challenge': challenge, 'challenge_type': challenge_type,
                                                     'right_answer': right_answer, 'options': options}},
                        alien_id: {'destinationName': destinationName, 'destinationCoords': destinationCoords,
                                   'challenge': {'challenge': challenge, 'challenge_type': challenge_type,
                                                 'right_answer': right_answer, 'options': options}},
                        wizard_id: {'destinationName': destinationName, 'destinationCoords': destinationCoords,
                                    'challenge': {'challenge': challenge, 'challenge_type': challenge_type,
                                                  'right_answer': right_answer, 'options': options}},
                        adventurer_id: {'destinationName': destinationName, 'destinationCoords': destinationCoords,
                                        'challenge': {'challenge': challenge, 'challenge_type': challenge_type,
                                                      'right_answer': right_answer, 'options': options}}}
        else:
            one_json = {detective_id: {'destinationName': destinationName, 'destinationCoords': destinationCoords,
                                       'challenge': {'challenge': challenge, 'challenge_type': challenge_type,
                                                     'right_answer': right_answer}},
                        alien_id: {'destinationName': destinationName, 'destinationCoords': destinationCoords,
                                   'challenge': {'challenge': challenge, 'challenge_type': challenge_type,
                                                 'right_answer': right_answer}},
                        wizard_id: {'destinationName': destinationName, 'destinationCoords': destinationCoords,
                                    'challenge': {'challenge': challenge, 'challenge_type': challenge_type,
                                                  'right_answer': right_answer}},
                        adventurer_id: {'destinationName': destinationName, 'destinationCoords': destinationCoords,
                                        'challenge': {'challenge': challenge, 'challenge_type': challenge_type,
                                                      'right_answer': right_answer}}}
        
    return one_json
