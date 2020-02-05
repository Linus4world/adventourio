from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask import request
import json
from all_answers_fcn import *
from game import *
from mocks_and_dummies import *


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

game = Game(number_of_players=1, number_of_pages=3*5, number_of_dummy_players=3)
SUCCESS = json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
challenges = {}

# ---------- For debugging purposes: ----------
debug_mode = False  # Default: False
player_input_mock = {}
challenge_outcome_db = True
# ---------------------------------------------


@app.route('/')
@cross_origin()
def hello_world():
    return {'hello': 'Hello, World!'}


@app.route('/questionnaire', methods=['GET'])
def send_questionnaire():
    with open("questionnaire.json", 'r', encoding='utf-8') as questionnaire:
        return json.load(questionnaire)


@app.route('/join/<player_id>', methods=['POST'])
def join(player_id):
    if not debug_mode:
        player_input = request.get_json()
    else:
        player_input = player_input_mock

    if game.is_full():
        return abort('Game is full!')

    # Add Player
    game.add_player(player_id, player_input)
    # game.ready_queue += 1  # !!!!! FOR TESTING !!!!! DELETE/COMMENT LATER !!!!!

    if game.is_full():

        # !!START THE GAME!!
        game.start_game()

    if not debug_mode and game.wait_for_game_ready():
        return json.dumps({"playerNames": game.get_player_names(),
                           "character": game.players[player_id].get_character_name()})
    if not debug_mode:
        return abort('No other players found :(')

@app.route('/stage/<player_id>', methods=['POST'])
def get_next_story_section(player_id):
    global challenges
    if not debug_mode:
        player_data = request.get_json()
    else:
        player_data = player_input_mock

    challenge_outcome = None
    player_location = None
    if 'challengeOutcome' in player_data:
        challenge_outcome = player_data['challengeOutcome']
    if 'playerLocation' in player_data:
        game.get_player(player_id).geo_location = player_data['playerLocation']

    if game.is_game_ready():

        # Get the challenges:
        challenges = new_place(game)

        game.ready_to_play = True
        print('Open')
        game.current_chapter += 1

    # Wait for other players to finish their challenge
    if not debug_mode and game.wait_for_game_ready():
        story_content = game.get_next_story_section(player_id, challenge_outcome)
        if not challenges:
            return json.dumps(story_content)
        challenges[player_id].update(story_content)
        return json.dumps(challenges[player_id])
    if not debug_mode:
        return abort('MAX_TIMEOUT')


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

    if not debug_mode:
        app.run()
    else:
        # ---------- Simulating what is happening in the front end ----------

        # ---------- Adding players: ----------
        player_input_mock = mock_input[0]
        join('00')

        player_input_mock = mock_input[1]
        join('01')

        player_input_mock = mock_input[2]
        join('02')

        player_input_mock = mock_input[3]
        join('03')

        # # Printing character assignment
        # for player_id in game.players.keys():
        #     print(player_id, game.players[player_id].character.name)

        # ---------- Getting the next story section: ----------

        print(game.get_next_story_section('02', True)['story'])
        print(game.get_next_story_section('02', True)['story'])
        # print(game.get_next_story_section('02', True)['story'])
        # print(game.get_next_story_section('02', True)['story'])
        # print(game.get_next_story_section('02', True)['story'])
        # print(game.get_next_story_section('02', True)['story'])
        # print(game.get_next_story_section('02', True)['story'])

        # The next few lines simulate what we would get from the front end
        # story_section = get_next_story_section(player_id='00')
        # print(story_section)

        # story_section = get_next_story_section(player_id='00')
        # print(story_section)
        #
        # story_section = get_next_story_section(player_id='00')
        # print(story_section)
