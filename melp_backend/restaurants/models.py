from melp_backend import db, ma
import uuid


# Restaurant Class/Model
class Restaurant(db.Model):
    id = db.Column(db.String(45), primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    site = db.Column(db.String(150))
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

    def __init__(self, rating, name, site, email, phone, street, city, state, lat=None, lng=None, id=uuid.uuid1()):
        self.id = id
        self.rating = rating
        self.name = name
        self.site = site
        self.email = email
        self.phone = phone
        self.street = street
        self.city = city
        self.state = state
        self.lat = lat
        self.lng = lng


# Restaurant Schema
class RestaurantSchema(ma.Schema):
    class Meta:
        fields = ('id', 'rating', 'name', 'site', 'id', 'email', 'phone', 'street', 'city', 'state', 'lat', 'lng')


# Init schema
restaurant_schema = RestaurantSchema()
restaurants_schema = RestaurantSchema(many=True)
