import numpy
import json
import random
from utils import *

class Character:
    def __init__(self, id_player, name):
        self.id_player = id_player
        self.name = name

class Adventurer(Character):
    description = "drunk"


class Alien(Character):
    description = "academic"


class Wizard(Character):
    description = "foreign cultures"


class Detective(Character):
    description = "break-free"


def get_character_assignment(answers):
    adventurer = Adventurer('0', 'player')
    alien = Alien('0', 'player')
    wizard = Wizard('0', 'player')
    detective = Detective('0', 'player')

    answers = json.loads(answers)

    points_id = [dict(), dict(), dict(), dict()]

    for i in range(0, 4):
        points_id[i]['id'] = answers['all_answers'][i]['id']
        points_id[i]['name'] = answers['all_answers'][i]['name']
        points_id[i]['points_adventurer'] = 0
        points_id[i]['points_alien'] = 0
        points_id[i]['points_wizard'] = 0
        points_id[i]['points_detective'] = 0

    # calculating the answers into points for specific characters for every person
    a = 0
    for answer in answers['all_answers']:
        if answer['answers'][3] == 'Adventurer/action':
            points_id[a]['points_adventurer'] = points_id[a]['points_adventurer'] + 1
        elif answer['answers'][3] == 'Science-fiction':
            points_id[a]['points_alien'] = points_id[a]['points_alien'] + 1
        elif answer['answers'][3] == 'Fantasy':
            points_id[a]['points_wizard'] = points_id[a]['points_wizard'] + 1
        elif answer['answers'][3] == 'crime':
            points_id[a]['points_detective'] = points_id[a]['points_detective'] + 1
        if answer['answers'][4] == 'To experience other cultures':
            points_id[a]['points_wizard'] = points_id[a]['points_wizard'] + 1
        elif answer['answers'][4] == "Because it's fun":
            points_id[a]['points_adventurer'] = points_id[a]['points_adventurer'] + 1
        elif answer['answers'][4] == 'To get away from where I normally live':
            points_id[a]['points_detective'] = points_id[a]['points_detective'] + 1
        elif answer['answers'][4] == 'To get some more academic experience':
            points_id[a]['points_alien'] = points_id[a]['points_alien'] + 1
        if answer['answers'][5] == 'Deutsches Museum':
            points_id[a]['points_alien'] = points_id[a]['points_alien'] + 1
        elif answer['answers'][5] == 'Oktoberfest':
            points_id[a]['points_adventurer'] = points_id[a]['points_adventurer'] + 1
        elif answer['answers'][5] == 'any restaurant with typical German cuisine':
            points_id[a]['points_wizard'] = points_id[a]['points_wizard'] + 1
        elif answer['answers'][5] == 'none of the above':
            points_id[a]['points_detective'] = points_id[a]['points_detective'] + 1
        if answer['answers'][6] == 'mostly friends from the university':
            points_id[a]['points_alien'] = points_id[a]['points_alien'] + 1
        elif answer['answers'][6] == 'lots of people from Germany':
            points_id[a]['points_detective'] = points_id[a]['points_detective'] + 1
        elif answer['answers'][6] == 'friends who came here with me':
            points_id[a]['points_adventurer'] = points_id[a]['points_adventurer'] + 1
        elif answer['answers'][6] == "no one in particular, people I've met here and there":
            points_id[a]['points_wizard'] = points_id[a]['points_wizard'] + 1
        a = a + 1

    """ used for debugging
    for points in points_id:
        print('player')
        print(points['id'])
        print('adventurer')
        print(points['points_adventurer'])
        print('alien')
        print(points['points_alien'])
        print('detective')
        print(points['points_detective'])
        print('wizard')
        print(points['points_wizard'])
    """

    # list of all
    all_adventurer_points = [0, 0, 0, 0]
    all_alien_points = [0, 0, 0, 0]
    all_wizard_points = [0, 0, 0, 0]
    all_detective_points = [0, 0, 0, 0]

    chosen = numpy.array([1, 1, 1, 1])
    chosen_characters = [1, 1, 1, 1]  # adventurer, alien, wizard, detective
    for i in range(0, 4):
        all_adventurer_points[i] = points_id[i]['points_adventurer']
        all_alien_points[i] = points_id[i]['points_alien']
        all_wizard_points[i] = points_id[i]['points_wizard']
        all_detective_points[i] = points_id[i]['points_detective']
    print(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points)

    count = 0
    for j in range(0, 4):
        if numpy.amax(all_adventurer_points) >= numpy.amax(all_alien_points) and chosen_characters[0] == 1:
            if numpy.amax(all_adventurer_points) >= numpy.amax(all_wizard_points) and chosen_characters[0] == 1:
                if numpy.amax(all_adventurer_points) >= numpy.amax(all_detective_points) and chosen_characters[0] == 1:
                    # max points adventurer
                    [all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, adventurer,
                     chosen] = \
                        maxAdventurer(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points,
                                      points_id, adventurer, chosen)
                    chosen_characters[0] = 0
                elif chosen_characters[3] == 1:
                    # max points detective
                    [all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, detective,
                     chosen] = \
                        maxDetective(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points,
                                     points_id, detective, chosen)
                    chosen_characters[3] = 0
            elif numpy.amax(all_wizard_points) >= numpy.amax(all_detective_points) and chosen_characters[2] == 1:
                # max points wizard
                [all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, wizard, chosen] = \
                    maxWizard(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points,
                              points_id, wizard, chosen)
                chosen_characters[2] = 0
            elif chosen_characters[3] == 1:
                # max points detective
                [all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, detective, chosen] = \
                    maxDetective(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points,
                                 points_id, detective, chosen)
                chosen_characters[3] = 0
        elif numpy.amax(all_alien_points) >= numpy.amax(all_wizard_points) and chosen_characters[1] == 1:
            if numpy.amax(all_alien_points) >= numpy.amax(all_detective_points) and chosen_characters[1] == 1:
                # max points alien
                [all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, alien, chosen] = \
                    maxAlien(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points,
                             points_id, alien, chosen)
                chosen_characters[1] = 0
            elif chosen_characters[3] == 1:
                # max points detective
                [all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, detective, chosen] = \
                    maxDetective(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points,
                                 points_id, detective, chosen)
                chosen_characters[3] = 0
        elif numpy.amax(all_wizard_points) >= numpy.amax(all_detective_points) and chosen_characters[2] == 1:
            # max points wizard
            [all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, wizard, chosen] = \
                maxWizard(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, points_id,
                          wizard, chosen)
            chosen_characters[2] = 0
        elif chosen_characters[3] == 1:
            # max points detective
            [all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, detective, chosen] = \
                maxDetective(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points,
                             points_id, detective, chosen)
            chosen_characters[3] = 0

    character_assignment = {
        alien.id_player: 'alien',
        adventurer.id_player: 'adventurer',
        detective.id_player: 'detective',
        wizard.id_player: 'wizard'
    }
    return character_assignment


def maxAdventurer(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, points_id,
                  adventurer, chosen):
    count = 0
    # most points adventurer
    # in case of there being only one person with the highest amount for points for the character, instant assignment
    if len(numpy.where(all_adventurer_points == numpy.amax(all_adventurer_points))[0]) == 1:
        for points in points_id:
            if points['points_adventurer'] == numpy.amax(all_adventurer_points):
                adventurer.id_player = points['id']
                adventurer.name = points['name']
                all_alien_points[count] = 0
                all_wizard_points[count] = 0
                all_detective_points[count] = 0
                chosen[count] = 0
                break
            count = count + 1
    # in case of there being more than one people with the same amount of highest points, random assignment
    else:
        n = random.randint(1, len(numpy.where(all_adventurer_points == numpy.amax(all_adventurer_points))[0]))
        if numpy.amax(all_adventurer_points) == 0 and len(
                numpy.where(all_adventurer_points == numpy.amax(all_adventurer_points))[0]) == 4:
            n = len(numpy.where(1 == chosen)[0])
        a = 0
        for points in points_id:
            if points['points_adventurer'] == numpy.amax(all_adventurer_points):
                if chosen[count] == 1:
                    a = a + 1
                    if a == n:
                        adventurer.id_player = points['id']
                        adventurer.name = points['name']
                        all_alien_points[count] = 0
                        all_wizard_points[count] = 0
                        all_detective_points[count] = 0
                        chosen[count] = 0
                        break
            count = count + 1
    all_adventurer_points = [0, 0, 0, 0]
    return all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, adventurer, chosen


def maxDetective(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, points_id, detective,
                 chosen):
    count = 0
    if len(numpy.where(all_detective_points == numpy.amax(all_detective_points))[0]) == 1:
        for points in points_id:
            if points['points_detective'] == numpy.amax(all_detective_points):
                detective.id_player = points['id']
                detective.name = points['name']
                all_alien_points[count] = 0
                all_wizard_points[count] = 0
                all_adventurer_points[count] = 0
                chosen[count] = 0
                break
            count = count + 1
    # in case of there being more than one people with the same amount of highest points, random assignment
    else:
        a = numpy.amax(all_detective_points)
        n = random.randint(1, len(numpy.where(all_detective_points == numpy.amax(all_detective_points))[0]))
        if numpy.amax(all_detective_points) == 0 and len(
                numpy.where(all_detective_points == numpy.amax(all_detective_points))[0]) == 4:
            n = len(numpy.where(1 == chosen)[0])
        a = 0
        for points in points_id:
            if points['points_detective'] == numpy.amax(all_detective_points):
                if chosen[count] == 1:
                    a = a + 1
                    if a == n:
                        detective.id_player = points['id']
                        detective.name = points['name']
                        all_alien_points[count] = 0
                        all_wizard_points[count] = 0
                        all_adventurer_points[count] = 0
                        chosen[count] = 0
                        break
            count = count + 1
    all_detective_points = [0, 0, 0, 0]
    return all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, detective, chosen


def maxAlien(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, points_id, alien,
             chosen):
    count = 0
    # most points alien
    # in case of there being only one person with the highest amount for points for the character, instant assignment
    if len(numpy.where(all_alien_points == numpy.amax(all_alien_points))[0]) == 1:
        for points in points_id:
            if points['points_alien'] == numpy.amax(all_alien_points):
                alien.id_player = points['id']
                alien.name = points['name']
                all_adventurer_points[count] = 0
                all_wizard_points[count] = 0
                all_detective_points[count] = 0
                chosen[count] = 0
                break
            count = count + 1
    # in case of there being more than one people with the same amount of highest points, random assignment
    else:
        n = random.randint(1, len(numpy.where(all_alien_points == numpy.amax(all_alien_points))[0]))
        # if all people have zero points
        if numpy.amax(all_alien_points) == 0 and len(
                numpy.where(all_alien_points == numpy.amax(all_alien_points))[0]) == 4:
            n = len(numpy.where(1 == chosen)[0])
        a = 0
        for points in points_id:
            if points['points_alien'] == numpy.amax(all_alien_points):
                if chosen[count] == 1:
                    a = a + 1
                    if a == n:
                        alien.id_player = points['id']
                        alien.name = points['name']
                        all_adventurer_points[count] = 0
                        all_wizard_points[count] = 0
                        all_detective_points[count] = 0
                        chosen[count] = 0
                        break
            count = count + 1
    all_alien_points = [0, 0, 0, 0]
    return all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, alien, chosen


def maxWizard(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, points_id, wizard,
              chosen):
    count = 0
    # most points wizard
    # in case of there being only one person with the highest amount for points for the character, instant assignment
    if len(numpy.where(all_wizard_points == numpy.amax(all_wizard_points))[0]) == 1:
        for points in points_id:
            if points['points_wizard'] == numpy.amax(all_wizard_points):
                wizard.id_player = points['id']
                wizard.name = points['name']
                all_alien_points[count] = 0
                all_adventurer_points[count] = 0
                all_detective_points[count] = 0
                chosen[count] = 0
                break
            count = count + 1
    # in case of there being more than one people with the same amount of highest points, random assignment
    else:
        n = random.randint(1, len(numpy.where(all_wizard_points == numpy.amax(all_wizard_points))[0]))
        if numpy.amax(all_adventurer_points) == 0 and len(
                numpy.where(all_adventurer_points == numpy.amax(all_adventurer_points))[0]) == 4:
            n = len(numpy.where(1 == chosen)[0])
        a = 0
        for points in points_id:
            if points['points_wizard'] == numpy.amax(all_wizard_points):
                if chosen[count] == 1:
                    a = a + 1
                    if a == n:
                        wizard.id_player = points['id']
                        wizard.name = points['name']
                        all_alien_points[count] = 0
                        all_adventurer_points[count] = 0
                        all_detective_points[count] = 0
                        chosen[count] = 0
                        break
            count = count + 1
    all_wizard_points = [0, 0, 0, 0]

    return all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, wizard, chosen


if __name__ == '__main__':
    ch = get_character_assignment(answers2)
    print(ch)