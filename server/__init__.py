""" A small flask Hello World """
import os
from flask import Flask, jsonify, request

APP = Flask(__name__)

# Load file based configuration overrides if present
if os.path.exists(os.path.join(os.getcwd(), 'config.py')):
    APP.config.from_pyfile(os.path.join(os.getcwd(), 'config.py'))
else:
    APP.config.from_pyfile(os.path.join(os.getcwd(), 'config.env.py'))

APP.secret_key = APP.config['SECRET_KEY']

@APP.route('/', methods=["GET"])
def _index_get():
    return jsonify(status=200, response="OK")

@APP.route('/', methods=["POST"])
def _index_post():
    return jsonify(request.json)
