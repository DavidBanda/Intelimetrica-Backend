from flask import request, jsonify, Blueprint
from melp_backend import db
from melp_backend.restaurants.models import Restaurant, restaurant_schema, restaurants_schema

restaurants = Blueprint('restaurants', __name__)


# GET all Restaurants
@restaurants.route('/restaurants', methods=['GET'])
def get_restaurants():
    all_restaurants = Restaurant.query.all()
    result = restaurants_schema.dump(all_restaurants)
    return jsonify(result)


# GET single Restaurant
@restaurants.route('/restaurant/<id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get_or_404(id)
    return restaurant_schema.jsonify(restaurant)
