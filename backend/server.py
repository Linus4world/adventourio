from flask import Flask
from flask_cors import CORS, cross_origin
from flask import jsonify

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def hello_world():
    return {'hello': 'Hello, World!'}


@app.route('/questionnaire')
def questions():
    with open("questionnaire.json") as questionnaire:
        return jsonify(questionnaire)


@app.route('/places')
def places():
    with open("places.json") as place:
        return jsonify(place)


if __name__ == '__main__':
    app.run()
