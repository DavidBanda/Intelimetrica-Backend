from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from melp_backend.config import Config
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
ma = Marshmallow(app)

from melp_backend.restaurants.routes import restaurants

app.register_blueprint(restaurants)

