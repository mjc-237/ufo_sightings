import csv
from flask import Flask, jsonify, abort

app = Flask(__name__)

# Load the CSV once at startup into memory
def load_sightings(filepath='ufo_sightings.csv'):
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

sightings = load_sightings()

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/json', methods=['GET'])
def send_json():
    data = {"message": "Hello!", "status": "Success"}
    return jsonify(data)

@app.route('/sightings', methods=['GET'])
def get_all_sightings():
    return jsonify(sightings)

@app.route('/sightings/<int:sighting_id>', methods=['GET'])
def get_sighting(sighting_id):
    for record in sightings:
        if int(record['id']) == sighting_id:
            return jsonify(record)
    abort(404, description=f"No sighting found with id {sighting_id}")

if __name__ == '__main__':
    app.run(debug=True)