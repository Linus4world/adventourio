from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
import json
import characters

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def hello_world():
    return {'hello': 'Hello, World!'}


@app.route('/questionnaire', methods=['GET', 'POTS'])
def givingquestionnaire():
    if request.method == 'GET':
        with open("questionnaire.json") as questionnaire:
            return json.load(questionnaire)
    elif request.method == 'POST':
        answers = request.get_json()
        return characters.character_assignment(answers)


@app.route('/places')
def places():
    with open("places.json") as place:
        return json.load(place)


if __name__ == '__main__':
    app.run()
