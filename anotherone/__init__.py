# app/__init__.py
from flask import Flask

application = Flask(__name__)
application.config.from_object('config')

# Always import the views module after the flask app object has been created
import anotherone.views
