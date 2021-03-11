from flask import Flask


# Flask
app = Flask(__name__)
app.config.from_pyfile('../config.py')
