from anotherone import app
from flask import render_template, url_for
import os
from random import choice

@app.route('/')
def index():
    selectedWisdom = randomImage()
    return render_template('index.html', selectedWisdom=selectedWisdom)

@app.route('/name/<name>')
def winmore(name):
    return render_template('hello.html', name=name)

def randomImage():
    nameList = os.listdir(os.path.join(app.static_folder, "img"))
    img_url = url_for('static', filename=os.path.join("img", choice(nameList)))
    return img_url