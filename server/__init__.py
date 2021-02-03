""" A small flask Hello World """
import os
import redis
from flask import Flask, jsonify, request

APP = Flask(__name__)

# Load file based configuration overrides if present
if os.path.exists(os.path.join(os.getcwd(), 'config.py')):
    APP.config.from_pyfile(os.path.join(os.getcwd(), 'config.py'))
else:
    APP.config.from_pyfile(os.path.join(os.getcwd(), 'config.env.py'))

APP.secret_key = APP.config['SECRET_KEY']

r = redis.Redis(host=APP.config['REDIS_HOST'], port=int(APP.config['REDIS_PORT']))

@APP.route('/', methods=["GET"])
def _index_get():
    return jsonify(status=200, response="OK")

@APP.route('/', methods=["POST"])
def _index_post():
    data = request.json
    r.set('max:val', data["max_val"])
    r.set('max:hash', data["max_hash"])
    return jsonify([r.get('max:val'), r.get('max:hash')])
