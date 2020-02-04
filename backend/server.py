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

game = Game(number_of_players=4, number_of_pages=6)
SUCCESS = json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

# ---------- For debugging purposes: ----------
wait = True  # Default: True
abortions_legal = True  # Default: True
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
    player_input = request.get_json()
    if game.is_full():
        return abort('Game is full!')

    # Add Player
    game.add_player(player_id, player_input)

    if game.is_full():
        # Package all the player answers into one object:
        all_player_answers = all_answers_function_v2(game.players)
        with open("challenges.json", 'r', encoding='utf-8') as file:
            challenges = file.read()
        # !!START THE GAME!!
        game.start_game(all_player_answers, challenges)

    if game.wait_for_game_ready():
        return json.dumps({"playerNames": game.get_player_names(),
                           "character": game.players[player_id].get_character_name()})
    if abortions_legal:
        return abort('No other players found :(')


@app.route('/stage/<player_id>', methods=['POST'])
def get_next_story_section(player_id):
    player_data = request.get_json()
    challenge_outcome = None
    player_location = None
    if hasattr(player_data, 'challenge_outcome'):
        challenge_outcome = player_data['challenge_outcome']
    if hasattr(player_data, 'playerLocation'):
        player_location = player_data['playerLocation']

    game.player_challenge_outcome[player_id] = challenge_outcome
    if game.is_game_ready():
        # At this point all player outcomes are stored in game.player_challenge_outcome
        # TODO call Agatas function with all player outcomes
        # This will be only called once for the last player!
        game.ready_to_play = True

    # Wait for other players to finish their challenge
    if game.wait_for_game_ready():
        # TODO Here the next story section for each player should be stored in game.player_next_chapter
        # We can simply do:
        # 
        # return game.player_next_chapter[player_id]
        story_section = game.get_next_story_section(player_id, challenge_outcome)
        return story_section

    if abortions_legal:
        return abort('MAX_TIMEOUT')


@app.route('/here/<player_id>')
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

    app.run()

    # ---------- Simulating what is happening in the front end ----------

    # ---------- Adding players: ----------
    # answers = dict(name='CARLOS I', answers=json.loads(answers2)['all_answers'][0])
    # join('00', answers)
    #
    # answers = dict(name='CARLOS II', answers=json.loads(answers2)['all_answers'][0])
    # join('01', answers)
    #
    # answers = dict(name='CARLOS II', answers=json.loads(answers2)['all_answers'][0])
    # join('02', answers)
    #
    # answers = dict(name='CARLOS IV', answers=json.loads(answers2)['all_answers'][0])
    # join('03', answers)
    #
    # # Printing character assignment
    # for player_id in game.players.keys():
    #     print(player_id, game.players[player_id].character.name)
    #
    # # ---------- Getting the next story section: ----------
    #
    # # The next few lines simulate what we would get from the front end
    # story_section = get_next_story_section(player_id='00', challenge_outcome=True)
    # print(story_section['story_text'], story_section['challenge'])
    #
    # story_section = get_next_story_section(player_id='00', challenge_outcome=True)
    # print(story_section['story_text'], story_section['challenge'])
    #
    # story_section = get_next_story_section(player_id='00', challenge_outcome=True)
    # print(story_section['story_text'], story_section['challenge'])
