from flask import request, jsonify, Blueprint
from melp_backend import db
from math import sqrt
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


# Create Restaurant
@restaurants.route('/restaurant', methods=['POST'])
def add_restaurant():
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

    new_restaurant = Restaurant(rating, name, site, email, phone, street,
                                city, state, lat, lng)
    db.session.add(new_restaurant)
    db.session.commit()

    return restaurant_schema.jsonify(new_restaurant)


# GET Close Restaurants
@restaurants.route('/restaurants/statistics', methods=['GET'])
def get_close_restaurants():
    lat = float(request.args.get('latitude'))
    lng = float(request.args.get('longitude'))
    rad = float(request.args.get('radius'))
    count = 0
    avg_rating = 0
    std = 0
    rating = []

    all_restaurants = Restaurant.query.all()

    for restaurant in all_restaurants:
        base = abs(restaurant.lat - lat)
        height = abs(restaurant.lng - lng)
        hypo = sqrt((base**2)+(height**2))
        if hypo <= rad:
            count += 1
            avg_rating += restaurant.rating
            rating.append(restaurant.rating)

    avg_rating /= count  # get average rating

    # Standard deviation of rating of restaurants inside the circle
    for rate in rating:
        dev_std = (rate - avg_rating)**2
        std += dev_std
    std /= count - 1

    return jsonify({'count': count, 'avg': avg_rating, 'std': std})
