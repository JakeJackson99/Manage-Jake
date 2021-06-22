from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from config import Config


# Flask
app = Flask(__name__)
app.config.from_object(Config)


# SQLAlchemy & Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)
