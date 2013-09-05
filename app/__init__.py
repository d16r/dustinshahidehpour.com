from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)

flatpages = FlatPages(app)
freezer = Freezer(app)

app.config.from_object('config')
from app import views
