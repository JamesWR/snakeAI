from flask import Flask
from flask import jsonify
from flask import request
from safe_snake import move
import json
from util.snake_squares import snake_squares

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def index():
    return 'Hi there'

@app.route('/move', methods = ['POST'])
def doMove():
    f = open("board.json", "w")
    f.write(json.dumps(request.json))
    return jsonify(move(request.json))

@app.route('/start', methods = ['POST'])
def start():
    return jsonify({ 'color': "#00937b" })

@app.route('/end', methods = ['POST'])
def end():
    return ''

@app.route('/ping', methods = ['POST'])
def ping():
    return 'You found me'

if __name__ == "__main__":
    app.run()
