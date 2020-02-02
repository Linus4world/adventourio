from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask import request
import json
from session import Session
from assign_characters import character_assignment
from all_answers_fcn import all_answers_function
#from destination_challenge_assingment import new_place
from all_answers_fcn import placesCategory

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# TODO change the param to 4 for real scenario!
session = Session(4)
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
    if session.isReady():
        all_answers = all_answers_function(session)
        with open("challenges.json", 'r', encoding='utf-8') as file:
            places = file.read()
        session.setPlacesCategory(placesCategory(all_answers, places))
        session.setCharacters(character_assignment(all_answers))
    if session.wait_for_session_ready():
        return json.dumps({"playerNames": session.playerNames, "character": session.getCharacter(id)})
    return abort('No other players found :(')


@app.route('/stage/<id>', methods = ['POST'])
def next_sub_stage(id):
    session.challengeOutcome[id] = request.get_json()

    global session
    if session.isReady():
        # TODO call Esteban function
        # session.playerNextChapter = ...
        session.readyToPlay = True
    if session.wait_for_session_ready():
        return session.playerNextChapter[id]
    return abort('MAX_TIMEOUT')
#     return json.dumps({
#         "story": [
#             'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas scelerisque urna dolor, ac pellentesque neque mollis vel. Etiam nec semper nulla. In hac habitasse platea dictumst. Proin fermentum quis urna sit amet porta. Nunc sed feugiat orci. Quisque leo magna, scelerisque et ipsum vitae, volutpat egestas sapien. Quisque metus enim, vestibulum nec viverra gravida, elementum ut dolor.',
#             'Etiam efficitur arcu vitae enim tristique fermentum. Donec sit amet cursus ligula. Mauris facilisis sollicitudin cursus. Aenean eu lacus tortor. Ut dapibus, leo a molestie blandit, sapien eros vestibulum metus, sit amet suscipit felis nunc in augue. Aenean a rhoncus magna. Nullam elementum quam orci, nec mattis mauris dignissim non. Cras pellentesque eget tellus quis mattis. Nullam at leo a enim imperdiet bibendum. Donec volutpat dolor vel lectus molestie, ac tristique arcu varius. Vestibulum blandit maximus massa, eget blandit enim. Cras id ligula dolor. Cras eget sem sed est convallis vulputate. Curabitur consectetur nunc quam, vitae pharetra ipsum venenatis vel.'
#             ],
#         "destinationCoords": [48.149116,11.567532],
#         "destinationName": "TUM Stammgelände",
#         "challenge": {
#             "challenge": 'Was ist ein Wolpertinger?',
#             "challenge_type": 1,
#             "options": [
#                 'Ein Wolf',
#                 'Ein Hase',
#                 'Ein Vogel',
#                 'Ein Fabelwesen'
#                 ],
#                 "right_answer": 'Ein Fabelwesen'
#         }
#    })


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
