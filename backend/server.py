from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
import json
from characters import character_assignment

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

SUCCESS = json.dumps({'success':True}), 200, {'ContentType':'application/json'}


@app.route('/')
@cross_origin()
def hello_world():
    return {'hello': 'Hello, World!'}


@app.route('/questionnaire', methods=['GET', 'POST'])
def givingquestionnaire():
    if request.method == 'GET':
        with open("questionnaire.json", 'r', encoding='utf-8') as questionnaire:
            return json.load(questionnaire)
    elif request.method == 'POST':
        answers = request.get_json()
        # character_assignment(answers)
        return SUCCESS


@app.route('/places')
def places():
    with open("places.json") as place:
        return json.load(place)

@app.route('/join/<id>')
def join(id):
   return SUCCESS

@app.route('/quest/<id>')
def next_quest(id):
   return json.dumps({
       "story": ['One', 'Two'],
       "goalLocation": {
           "lat": 48.2427456,
           "long": 11.6597312
       }
   })


if __name__ == '__main__':
    app.run()
