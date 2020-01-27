from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask import request
import json
from session import Session
from characters import character_assignment

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# TODO change the param to 4 for real scenario!
session = Session(2)
SUCCESS = json.dumps({'success':True}), 200, {'ContentType':'application/json'}


@app.route('/')
@cross_origin()
def hello_world():
    return {'hello': 'Hello, World!'}


@app.route('/questionnaire', methods=['GET'])
def givingquestionnaire():
    with open("questionnaire.json", 'r', encoding='utf-8') as questionnaire:
        return json.load(questionnaire)

@app.route('/join/<id>', methods = ['POST'])
def join(id):
    answers = request.get_json()

    global session
    if session.isFull():
        return abort('Session is full!')
    session.addPlayer(id, answers["name"], answers["answers"])
    doCharacterAssignment = session.isFull()
    if session.wait_for_full_session():
        if doCharacterAssignment:
            pass
            # TODO @Agata prepare all_answers object
            # 
            # all_answers = ...
            # character_assignment(all_answers)

        return json.dumps({"playerNames": session.playerNames})
    return abort('No other players found :(')

@app.route('/stage/<id>', methods = ['POST'])
def next_sub_stage(id):
    challengeOutcome = request.get_json()
    return json.dumps({
        "story": ['One', 'Two'],
        "destinationCoords": [48.149116,11.567532],
        "destinationName": "TUM Stammgelände",
        "challenge": {
            "challenge": 'Was ist ein Wolpertinger?',
            "challenge_type": 1,
            "answers": [
                'Ein Wolf',
                'Ein Hase',
                'Ein Vogel',
                'Ein Fabelwesen'
                ],
                "right_answer": 'Ein Fabelwesen'
        }
   })

@app.route('/here/<id>')
def here(id):
   return SUCCESS

def abort(message: str):
    """
    returns an error response with the given message
    """
    response = jsonify({'message': message})
    response.status_code = 400
    return response

if __name__ == '__main__':
    app.run()
