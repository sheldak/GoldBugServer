from app import app
from flask import Flask, request, jsonify
import json

@app.route('/', methods = ['POST'])
@app.route('/index')
def index():
    f = open("data.json", 'w')

    content = request.get_json(silent=True)
    f.write(json.dumps(content))

    f.close()
    return str(content)
