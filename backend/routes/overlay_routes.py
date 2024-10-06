from flask import Blueprint, request, jsonify
from config.db import get_db
from bson import ObjectId

overlay_routes = Blueprint('overlay_routes', __name__)
db = get_db()
overlay_collection = db['overlays']

# Define CRUD routes here (as in the previous example)
