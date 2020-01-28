import math

class Player:
    # destination - the places of the current stage, player assumed to be there
    # stage - current stage in the story
    def __init__(self, destination, stage):
        self.destination = destination
        self.stage = stage


def new_place(player1, player2, places_in):

    destination1 = player1.destination
    destination2 = player2.destination

    # calculate middle point between two players
    if destination1[0] >= destination2[0]:
        new_latt = destination1[0]-(destination1[0] - destination2[0])/2
    else:
        new_latt = destination2[0] - (destination2[0] - destination1[0])/2

    if destination1[1] >= destination2[1]:
        new_long = destination1[1] - (destination1[1] - destination2[1])/2
    else:
        new_long = destination2[1] - (destination2[1] - destination1[1])/2

    print(places_in)
    r_old = 0
    place_name = "null"
    place_id = 0
    for stages in places_in['places']:
        if stages['stage'] == (player1.stage + 1) and stages['stage'] == (player2.stage + 1):
            for place in stages['place']:
                r1 = math.pow(place['coordinates'][0] - new_latt, 2)
                r2 = math.pow(place['coordinates'][1] - new_long, 2)
                r = math.sqrt(r1+r2)
                if r < r_old or r_old == 0:
                    place_name = place['title']
                    place_id = place['id']
                    r_old = r

    return place_name, place_id


