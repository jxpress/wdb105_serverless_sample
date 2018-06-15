# coding: utf-8

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'message': 'Hello serverless WSGI world!!'})

# ルート以外のリクエストはここで受ける
@app.route('/<path:path>')
def any_path(path):
    return jsonify({'message': f'Here: /{path}'})

