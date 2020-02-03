from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask import request
import json
from session import Session
from assign_characters import get_character_assignment
from all_answers_fcn import store_all_player_answers_in_one_file
#from destination_challenge_assingment import new_place
from all_answers_fcn import placesCategory
from game import *
from utils import *
from mocks_and_dummies import *


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

game = Game(number_of_players=4, number_of_pages=6)
# session = Session(4)
SUCCESS = json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/')
@cross_origin()
def hello_world():
    return {'hello': 'Hello, World!'}


@app.route('/questionnaire', methods=['GET'])
def send_questionnaire():
    with open("questionnaire.json", 'r', encoding='utf-8') as questionnaire:
        return json.load(questionnaire)


@app.route('/join/<id>', methods=['POST'])
def join(player_id, player_input=None):

    if player_input is None:
        player_input = request.get_json()

    if game.is_full():
        return abort('Session is full!')

    # Add Player
    game.add_player(player_id, player_input)

    if game.is_full():
        # Package all the player answers into one object:
        all_player_answers = store_all_player_answers_in_one_file(game.players)
        with open("challenges.json", 'r', encoding='utf-8') as file:
            challenges = file.read()

        # Set characters and set challenges
        game.start_game(all_player_answers, challenges)
    else:
        # TODO: LINUS: SEND A MESSAGE SAYING: "WAITING FOR OTHER PLAYERS TO JOIN..."
        # We cannot wait for each player unless we use threads... I think
        pass

    # if game.wait_for_session_ready():
    #     return json.dumps({"playerNames": session.playerNames, "character": session.getCharacter(player_id)})
    # return abort('No other players found :(')


@app.route('/stage/<id>', methods=['POST'])
def get_next_story_section(player_id, challenge_outcome=None):
    if challenge_outcome is None:
        challenge_outcome = request.get_json()
    story_section = game.get_next_story_section(player_id, challenge_outcome)
    return story_section

    #
    # # global session
    # if session.isReady():
    #     # session.playerNextChapter = ...
    #     session.readyToPlay = True
    #
    # if session.wait_for_session_ready():
    #     return session.playerNextChapter[id]
    # return abort('MAX_TIMEOUT')


@app.route('/here/<id>')
def here(player_id):
    return SUCCESS


def abort(message: str):
    """
    returns an error response with the given message
    """
    response = jsonify({'message': message})
    response.status_code = 400
    return response


if __name__ == '__main__':
    story = game.story
    story.setup_story()

    # app.run()

    # ---------- Simulating what is happening in the front end ----------

    # ---------- Adding players: ----------
    answers = dict(name='CARLOS I', answers=json.loads(answers2)['all_answers'][0])
    join('00', answers)

    answers = dict(name='CARLOS II', answers=json.loads(answers2)['all_answers'][0])
    join('01', answers)

    answers = dict(name='CARLOS II', answers=json.loads(answers2)['all_answers'][0])
    join('02', answers)

    answers = dict(name='CARLOS IV', answers=json.loads(answers2)['all_answers'][0])
    join('03', answers)

    # Printing character assignment
    for player_id in game.players.keys():
        print(player_id, game.players[player_id].character.name)

    # ---------- Getting the next story_segment: ----------

    # The next few lines simulate what we would get from the front end
    get_next_story_section(player_id='00', challenge_outcome=True)
    #
    get_next_story_section(player_id='00', challenge_outcome=True)
    #
    # get_next_story_section(player_id='00', challenge_outcome=True)
