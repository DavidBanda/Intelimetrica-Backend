from flask import request, jsonify, Blueprint
from melp_backend import db
from melp_backend.restaurants.models import Restaurant, restaurant_schema, restaurants_schema

restaurants = Blueprint('restaurants', __name__)


