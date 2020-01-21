import numpy
import json
import random

# mock json
answers1 = """
{
    "answers1": [
        {
            "id": "1",
            "answers": [
                "a",
                "a",
                "d",
                "d"
            ]
        },
        {
            "id": "2",
            "answers": [
                "a",
                "b",
                "b",
                "c"
            ]
        },
        {
            "id": "3",
            "answers": [
                "b",
                "c",
                "a",
                "a"
            ]
        },
        {
            "id": "4",
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
    "answers1": [
        {
            "id": "1",
            "answers": [
                "a",
                "a",
                "d",
                "d"
            ]
        },
        {
            "id": "2",
            "answers": [
                "a",
                "b",
                "b",
                "c"
            ]
        },
        {
            "id": "3",
            "answers": [
                "a",
                "b",
                "b",
                "c"
            ]
        },
        {
            "id": "4",
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


class Character:
    def __init__(self, id_player):
        self.id_player = id_player


class Adventurer(Character):
    # Exchange student that wants to get drunk and have fun:
    # - hedonist, egoist, spontaneous, carefree, fun loving, open
    # to new experiences, relaxed, extroverted, sociable, friendly, loud, physical,
    # reckless, passionate, simple minded, pragmatic, confident, flirty, brave, chivalrous (Adventure)
    description = "drunk"


class Alien(Character):
    # Exchange studentthat is in Munichfor academic / CV reasons:
    # studious, introverted, anxious, proud, responsible, shy, goal oriented, ambitious, non - independent,
    # easily overwhelmed, rational, careful, sheltered, family oriented, sullen, strategic (Science Fiction)
    description = "academic"


class Wizard(Character):
    # Exchange student interested in foreign cultures:
    # - curious, spontaneous, open-minded, liberal, creative, drifting, respectful, intellectual, confident, adventurous,
    # impatient, restless, ditzy, naive, sheltered, optimistic, excitable, emotional, empathetic, helpful (fantasy)
    description = "foreign cultures"


class Detective(Character):
    # Exchange student that wants to escape personal problems in home country/”break free” from his old ways:
    # anxious, melancholic, escapist, pensive, tense, introverted, imaginative, creative,
    # empathetic, easily overwhelmed, humble, introspective, idealistic, irresponsible,
    # sensitive, controlling, brave, self-sacrificing  (crime)
    description = "break-free"


def character_assignment(answers):
    adventurer = Adventurer('0')
    alien = Alien('0')
    wizard = Wizard('0')
    detective = Detective('0')

    # answers = json.loads(answers)
    points_id = [dict(), dict(), dict(), dict()]

    for i in range(0, 4):
        points_id[i]['id'] = answers['answers1'][i]['id']
        points_id[i]['points_adventurer'] = 0
        points_id[i]['points_alien'] = 0
        points_id[i]['points_wizard'] = 0
        points_id[i]['points_detective'] = 0

    # calculating the answers into points for specific characters for every person
    a = 0
    for answer in answers['answers1']:
        if answer['answers'][0] == 'a':
            points_id[a]['points_adventurer'] = points_id[a]['points_adventurer'] + 1
        elif answer['answers'][0] == 'b':
            points_id[a]['points_alien'] = points_id[a]['points_alien'] + 1
        elif answer['answers'][0] == 'c':
            points_id[a]['points_wizard'] = points_id[a]['points_wizard'] + 1
        elif answer['answers'][0] == 'd':
            points_id[a]['points_detective'] = points_id[a]['points_detective'] + 1
        if answer['answers'][1] == 'a':
            points_id[a]['points_wizard'] = points_id[a]['points_wizard'] + 1
        elif answer['answers'][1] == 'b':
            points_id[a]['points_adventurer'] = points_id[a]['points_adventurer'] + 1
        elif answer['answers'][1] == 'c':
            points_id[a]['points_detective'] = points_id[a]['points_detective'] + 1
        elif answer['answers'][1] == 'd':
            points_id[a]['points_alien'] = points_id[a]['points_alien'] + 1
        if answer['answers'][2] == 'a':
            points_id[a]['points_alien'] = points_id[a]['points_alien'] + 1
        elif answer['answers'][2] == 'b':
            points_id[a]['points_adventurer'] = points_id[a]['points_adventurer'] + 1
        elif answer['answers'][2] == 'c':
            points_id[a]['points_wizard'] = points_id[a]['points_wizard'] + 1
        elif answer['answers'][2] == 'd':
            points_id[a]['points_detective'] = points_id[a]['points_detective'] + 1
        if answer['answers'][3] == 'a':
            points_id[a]['points_alien'] = points_id[a]['points_alien'] + 1
        elif answer['answers'][3] == 'b':
            points_id[a]['points_detective'] = points_id[a]['points_detective'] + 1
        elif answer['answers'][3] == 'c':
            points_id[a]['points_adventurer'] = points_id[a]['points_adventurer'] + 1
        elif answer['answers'][3] == 'd':
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

    chosen = [1, 1, 1, 1]
    chosen_characters = [1, 1, 1, 1] # adventurer, alien, wizard, detective
    for i in range(0, 4):
        all_adventurer_points[i] = points_id[i]['points_adventurer']
        all_alien_points[i] = points_id[i]['points_alien']
        all_wizard_points[i] = points_id[i]['points_wizard']
        all_detective_points[i] = points_id[i]['points_detective']

    count = 0
    for j in range(0, 4):
        if numpy.amax(all_adventurer_points) >= numpy.amax(all_alien_points) and chosen_characters[0] == 1:
            if numpy.amax(all_adventurer_points) >= numpy.amax(all_wizard_points) and chosen_characters[0] == 1:
                if numpy.amax(all_adventurer_points) >= numpy.amax(all_detective_points) and chosen_characters[0] == 1:
                    # max points adventurer
                    [all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, adventurer, chosen] = \
                        maxAdventurer(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, points_id, adventurer, chosen)
                    chosen_characters[0] = 0
                elif chosen_characters[3] == 1:
                    # max points detective
                    [all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, detecctive, chosen] = \
                        maxDetective(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, points_id, detective, chosen)
                    chosen_characters[3] = 0
            elif numpy.amax(all_wizard_points) >= numpy.amax(all_detective_points) and chosen_characters[2] == 1:
                # max points wizard
                [all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, wizard, chosen] = \
                    maxWizard(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, points_id, wizard, chosen)
                chosen_characters[2] = 0
            elif chosen_characters[3] == 1:
                # max points detective
                [all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, detective, chosen] = \
                    maxDetective(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, points_id, detective, chosen)
                chosen_characters[3] = 0
        elif numpy.amax(all_alien_points) >= numpy.amax(all_wizard_points) and chosen_characters[1] == 1:
            if numpy.amax(all_alien_points) >= numpy.amax(all_detective_points) and chosen_characters[1] == 1:
                # max points alien
                [all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, alien, chosen] = \
                    maxAlien(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, points_id, alien, chosen)
                chosen_characters[1] = 0
            elif chosen_characters[3] == 1:
                # max points detective
                [all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, detective, chosen] = \
                    maxDetective(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, points_id, detective, chosen)
                chosen_characters[3] = 0
        elif numpy.amax(all_wizard_points) >= numpy.amax(all_detective_points) and chosen_characters[2] == 1:
            # max points wizard
            [all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, wizard, chosen] = \
                maxWizard(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, points_id, wizard, chosen)
            chosen_characters[2] = 0
        elif chosen_characters[3] == 1:
            # max points detective
            [all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, detective, chosen] = \
                maxDetective(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, points_id, detective, chosen)
            chosen_characters[3] = 0

    return adventurer, alien, wizard, detective


def maxAdventurer(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, points_id, adventurer, chosen ):
    count = 0
    # most points adventurer
    # in case of there being only one person with the highest amount for points for the character, instant assignment
    if len(numpy.where(all_adventurer_points == numpy.amax(all_adventurer_points))[0]) == 1:
        for points in points_id:
            if points['points_adventurer'] == numpy.amax(all_adventurer_points):
                adventurer.id_player = points['id']
                all_alien_points[count] = 0
                all_wizard_points[count] = 0
                all_detective_points[count] = 0
                chosen[count] = 0
                break
            count = count + 1
    # in case of there being more than one people with the same amount of highest points, random assignment
    else:
        n = random.randint(1, len(numpy.where(all_adventurer_points == numpy.amax(all_adventurer_points))[0]))
        if numpy.amax(all_adventurer_points) == 0 and len(numpy.where(all_adventurer_points == numpy.amax(all_adventurer_points))[0]) == 4:
            n = 1
        a = 0
        for points in points_id:
            if points['points_adventurer'] == numpy.amax(all_adventurer_points):
                if chosen[count] == 1:
                    a = a + 1
                    if a == n:
                        adventurer.id_player = points['id']
                        all_alien_points[count] = 0
                        all_wizard_points[count] = 0
                        all_detective_points[count] = 0
                        chosen[count] = 0
                        break
            count = count + 1
    all_adventurer_points = [0, 0, 0, 0]
    return all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, adventurer, chosen


def maxDetective(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, points_id, detective, chosen):
    count = 0
    if len(numpy.where(all_detective_points == numpy.amax(all_detective_points))[0]) == 1:
        for points in points_id:
            if points['points_detective'] == numpy.amax(all_detective_points):
                detective.id_player = points['id']
                all_alien_points[count] = 0
                all_wizard_points[count] = 0
                all_adventurer_points[count] = 0
                chosen[count] = 0
                break
            count = count + 1
    # in case of there being more than one people with the same amount of highest points, random assignment
    else:
        n = random.randint(1, len(numpy.amax(all_detective_points == numpy.amax(all_detective_points))[0]))
        if numpy.amax(all_detective_points) == 0 and len(numpy.where(all_detective_points == numpy.amax(all_detective_points))[0]) == 4:
            n = 1
        a = 0
        for points in points_id:
            if points['points_detective'] == numpy.amax(all_detective_points):
                if chosen[count] == 1:
                    a = a + 1
                    if a == n:
                        detective.id_player = points['id']
                        all_alien_points[count] = 0
                        all_wizard_points[count] = 0
                        all_adventurer_points[count] = 0
                        chosen[count] = 0
                        break
            count = count + 1
    all_detective_points = [0, 0, 0, 0]
    return all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, detective, chosen


def maxAlien(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, points_id, alien, chosen):
    count = 0
    # most points alien
    # in case of there being only one person with the highest amount for points for the character, instant assignment
    if len(numpy.where(all_alien_points == numpy.amax(all_alien_points))[0]) == 1:
        for points in points_id:
            if points['points_alien'] == numpy.amax(all_alien_points):
                alien.id_player = points['id']
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
        if numpy.amax(all_alien_points) == 0 and len(numpy.where(all_alien_points == numpy.amax(all_alien_points))[0]) == 4:
            n = 1
        a = 0
        for points in points_id:
            if points['points_alien'] == numpy.amax(all_alien_points):
                if chosen[count] == 1:
                    a = a + 1
                    if a == n:
                        alien.id_player = points['id']
                        all_adventurer_points[count] = 0
                        all_wizard_points[count] = 0
                        all_detective_points[count] = 0
                        chosen[count] = 0
                        break
            count = count + 1
    all_alien_points = [0, 0, 0, 0]
    return all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, alien, chosen


def maxWizard(all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, points_id, wizard, chosen):
    count = 0
    # most points wizard
    # in case of there being only one person with the highest amount for points for the character, instant assignment
    if len(numpy.where(all_wizard_points == numpy.amax(all_wizard_points))[0]) == 1:
        for points in points_id:
            if points['points_wizard'] == numpy.amax(all_wizard_points):
                wizard.id_player = points['id']
                all_alien_points[count] = 0
                all_adventurer_points[count] = 0
                all_detective_points[count] = 0
                chosen[count] = 0
                break
            count = count+1
    # in case of there being more than one people with the same amount of highest points, random assignment
    else:
        n = random.randint(1, len(numpy.where(all_wizard_points == numpy.amax(all_wizard_points))[0]))
        if numpy.amax(all_adventurer_points) == 0 and len(numpy.where(all_adventurer_points == numpy.amax(all_adventurer_points))[0]) == 4:
            n = 1
        a = 0
        for points in points_id:
            if points['points_wizard'] == numpy.amax(all_wizard_points):
                if chosen[count] == 1:
                    a = a + 1
                    if a == n:
                        wizard.id_player = points['id']
                        all_alien_points[count] = 0
                        all_adventurer_points[count] = 0
                        all_detective_points[count] = 0
                        chosen[count] = 0
                        break
            count = count + 1
    all_wizard_points = [0, 0, 0, 0]

    return all_adventurer_points, all_alien_points, all_wizard_points, all_detective_points, wizard, chosen