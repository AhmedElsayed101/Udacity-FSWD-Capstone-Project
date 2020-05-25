from flask import Flask
from database.models import *
import os



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL_LOCAL')                                   
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app=app)
