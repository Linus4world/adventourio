import json


def all_answers_function(session):
    all_answers = [dict(), dict(), dict(), dict()]
    for i in range(0, 4):
        all_answers[i]['id'] = session.playerIds[i]
        all_answers[i]['name'] = session.playerNames[i]
        all_answers[i]['answers'] = session.playerAnswers[i]

    all_answers = {'all_answers': all_answers}
    return json.dumps(all_answers)
