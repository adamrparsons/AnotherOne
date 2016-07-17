from anotherone import application
from flask import render_template, url_for
import os
from random import choice

@application.route('/')
def index():
    selectedWisdom = randomImage()
    return render_template('index.html', selectedWisdom=selectedWisdom)

@application.route('/name/<name>')
def winmore(name):
    return render_template('hello.html', name=name)

def randomImage():
    nameList = os.listdir(os.path.join(application.static_folder, "img"))
    img_url = url_for('static', filename=os.path.join("img", choice(nameList)))
    return img_url