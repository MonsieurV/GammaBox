from flask import Flask, render_template, request, jsonify
import json
from . import forward

app = Flask(__name__)
RADBOX_SETTINGS_FILE = 'settings.json'
forwarder = forward.Forwarder(RADBOX_SETTINGS_FILE)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/settings")
def settings():
    return render_template('settings.html')

# API.

@app.route("/api/settings", methods=['GET'])
def api_settings_get():
    with open(RADBOX_SETTINGS_FILE, 'rb') as f:
        return jsonify(json.load(f))

@app.route("/api/settings", methods=['POST'])
def api_settings_post():
    with open(RADBOX_SETTINGS_FILE, 'wb') as f:
        json.dump(request.get_json(), f)
    # TODO Use message passing.
    forwarder.reloadConfiguration()
    return '', 204
