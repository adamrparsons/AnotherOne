# app/__init__.py
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

# Always import the views module after the flask app object has been created
import anotherone.views