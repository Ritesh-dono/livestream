from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017/")
db = client['overlayDB']
overlay_collection = db['overlays']
@app.route('/overlays', methods=['POST'])
def create_overlay():
    new_overlay = request.json
    get_overlays.append(new_overlay)
    return jsonify(new_overlay), 201


@app.route('/overlays', methods=['GET'])
def get_overlays():
    return jsonify(get_overlays)

@app.route('/overlays/<int:overlay_id>', methods=['PUT'])
def update_overlay(overlay_id):
    updated_data = request.json
    get_overlays[overlay_id] = updated_data
    return jsonify(updated_data), 200


@app.route('/overlays/<int:overlay_id>', methods=['DELETE'])
def delete_overlay(overlay_id):
    deleted_overlay = get_overlays.pop(overlay_id)
    return jsonify(deleted_overlay), 200

if __name__ == '__main__':
    app.run(debug=True)