from flask import render_template
from mbtaCrTracker import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/train/locate', methods=['GET'])
def map():
    return render_template('locate.html')
