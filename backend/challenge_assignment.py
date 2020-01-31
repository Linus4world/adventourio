import math


class Player:
    # destination - the places of the current stage, player assumed to be there
    # stage - current stage in the story
    def __init__(self, destination, stage):
        self.destination = destination
        self.stage = stage


def select_a_challenge(page_variations, player):
    pass

def new_place(player1, player2, places_in):
    destination1 = player1.geo_location
    destination2 = player2.geo_location

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
    for stages in places_in['places']:
        if stages['stage'] == (player1.stage + 1) and stages['stage'] == (player2.stage + 1):
            for place in stages['place']:
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
    if challenge_type == 1:
        one_json = {'destinationName': destinationName, 'destinationCoords': destinationCoords,
                    'challenge': {'challenge': challenge, 'challenge_type': challenge_type,
                                  'right_answer': right_answer, 'options': options}}
    else:
        one_json = {'destinationName': destinationName, 'destinationCoords': destinationCoords,
                    'challenge': {'challenge': challenge, 'challenge_type': challenge_type,
                                  'right_answer': right_answer}}

    return one_json
