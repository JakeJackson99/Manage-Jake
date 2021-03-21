from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager

# Flask
app = Flask(__name__)
app.config.from_pyfile('../config.py')
