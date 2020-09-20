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


# DELETE single Restaurant
@restaurants.route('/restaurant/<id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get_or_404(id)
    db.session.delete(restaurant)
    db.session.commit()

    return restaurant_schema.jsonify(restaurant)


# UPDATE single Restaurant
@restaurants.route('/restaurant/<id>', methods=['PUT'])
def update_restaurant(id):
    restaurant = Restaurant.query.get_or_404(id)

    rating = request.json['rating']
    name = request.json['name']
    site = request.json['site']
    email = request.json['email']
    phone = request.json['phone']
    street = request.json['street']
    city = request.json['city']
    state = request.json['state']
    lat = request.json['lat']
    lng = request.json['lng']

    restaurant.rating = rating
    restaurant.name = name
    restaurant.site = site
    restaurant.email = email
    restaurant.phone = phone
    restaurant.street = street
    restaurant.city = city
    restaurant.state = state
    restaurant.lat = lat
    restaurant.lng = lng

    db.session.commit()

    return restaurant_schema.jsonify(restaurant)
