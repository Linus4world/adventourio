import json
import numpy
import random


# SAME FUNCTION AS all_answers_function, but adapted
def store_all_player_answers_in_one_file(players):
    all_answers = [dict(), dict(), dict(), dict()]
    for i, player_id in enumerate(players.keys()):
        all_answers[i]['id'] = player_id
        all_answers[i]['name'] = players[player_id].name
        all_answers[i]['answers'] = players[player_id].answers
    all_answers = {'all_answers': all_answers}
    return json.dumps(all_answers)


def all_answers_function(session):
    all_answers = [dict(), dict(), dict(), dict()]
    for i in range(0, 4):
        all_answers[i]['id'] = session.playerIds[i]
        all_answers[i]['name'] = session.playerNames[i]
        all_answers[i]['answers'] = session.playerAnswers[i]

    all_answers = {'all_answers': all_answers}
    return json.dumps(all_answers)


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


def placesCategory(all_answers, places):

    all_answers = json.loads(all_answers)
    places = json.loads(places)
    results = numpy.array([0,0,0]) # entertainment, uni, sightseeing
    max_res = 'null'
    places_result = dict()

    for answer in all_answers['all_answers']:
        if answer['answers'][0] == 'a':
            results[0] = results[0] + 1
        elif answer['answers'][0] == 'b':
            results[1] = results[1] + 1
        elif answer['answers'][0] == 'c':
            results[2] = results[2] + 1

    if len(numpy.where(results == numpy.amax(results))[0]) == 1:
        n = numpy.where(results == numpy.amax(results))[0]
        if n == 0:
            max_res = 'entertainment'
        elif n == 1:
            max_res = 'university'
        elif n == 2:
            max_res = 'sightseeing'
    else:
        a = random.randint(0, len(numpy.where(results == numpy.amax(results))[0]) - 1)
        n = numpy.where(results == numpy.amax(results))[0][a]
        if n == 0:
            max_res = 'entertainment'
        elif n == 1:
            max_res = 'university'
        elif n == 2:
            max_res = 'sightseeing'

    for place in places['places']:
        if place['category'] == max_res:
            places_result['stages'] = place['stages']
            break

    return places_result

"""
with open("places.json") as file:
    places = file.read()

print(questionnaire(answers3, places))
"""