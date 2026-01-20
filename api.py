from flask import Flask, request, jsonify
from scoring import score

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/predict", methods=["POST"])
def predict():
    payload = request.get_json(silent=True) or {}
    result = score(payload)
    return jsonify(result)

