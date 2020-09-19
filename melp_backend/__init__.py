from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from melp_backend.config import Config
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
ma = Marshmallow(app)
login_manager = LoginManager(app)

