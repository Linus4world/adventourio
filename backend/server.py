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
SUCCESS = json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

# ------------------  Set this according to your needs  ----------------
NUMBER_OF_PLAYERS = 1
NUMBER_OF_PAGES = 3*5
NUMBER_OF_DUMMY_PLAYERS = 3

game = None
challenges = {}

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
    player_input = request.get_json()
    if game.is_full():
        return abort('Game is full!')

    # Add Player
    game.add_player(player_id, player_input)
    if game.is_full():
        game.start_game()

    if game.wait_for_game_ready():
        return json.dumps({"playerNames": game.get_player_names(),
                           "character": game.players[player_id].get_character_name()})
    return abort('No other players found :(')

@app.route('/stage/<player_id>', methods=['POST'])
def get_next_story_section(player_id):
    global challenges
    player_data = request.get_json()

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
    if game.wait_for_game_ready():
        story_content = game.get_next_story_section(player_id, challenge_outcome)
        if not challenges:
            return json.dumps(story_content)
        challenges[player_id].update(story_content)
        return json.dumps(challenges[player_id])
    return abort('MAX_TIMEOUT')

@app.route('/leave/<player_id>')
def leave(player_id):
    global game
    if game.leave_game(player_id):
        print('All players left the game, restarting server...')
        setup()
    return SUCCESS

def setup():
    global game
    global challenges
    global NUMBER_OF_PLAYERS
    global NUMBER_OF_PAGES
    global NUMBER_OF_DUMMY_PLAYERS

    print('Setting up the server...')
    game = Game(number_of_players=NUMBER_OF_PLAYERS, number_of_pages=NUMBER_OF_PAGES, number_of_dummy_players=NUMBER_OF_DUMMY_PLAYERS)
    challenges = {}
    game.story.setup_story()
    print('Setup complete!')

def abort(message: str):
    """
    returns an error response with the given message
    """
    response = jsonify({'message': message})
    response.status_code = 400
    return response


if __name__ == '__main__':
    setup()
    app.run()
