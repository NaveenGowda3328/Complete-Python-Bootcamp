from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def json():
    marks = {
        "Naveen": 84,
        "Manoj": 86
    }
    values = [1, marks, 87]
    return jsonify(values)

app.run(debug=True)