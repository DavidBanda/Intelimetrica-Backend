from melp_backend import db


# Restaurant Class/Model
class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False, default=5)
    name = db.Column(db.String(100), nullable=False)
    site = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(10), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

    def __init__(self, rating, name, site, email, phone, street, city, state, lat=None, lng=None):
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
