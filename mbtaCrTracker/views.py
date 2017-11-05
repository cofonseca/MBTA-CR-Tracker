from flask import render_template, request, redirect
from mbtaCrTracker import app
#import sys

@app.route('/')
@app.route('/index')
def index():
    lines = [['Fairmount','Fairmount'],['Fitchburg','Fitchburg'],['Worcester','Framingham'],['Franklin','Franklin'],['Greenbush','Greenbush'],['Kingston','Kingston'],['Middleborough','Lakevile'],['Middleborough','Middleborough'],['Needham','Needham'],['Providence','Providence'],['Providence','Stoughton'],['Worcester','Worcester']]
    return render_template('index.html', lines=lines)

@app.route('/map', methods=['GET'])
def map():
    line = request.args.get('line')
    direction = request.args.get('direction')
    #print(line, file=sys.stdout)
    #print(direction, file=sys.stdout)
    #coords = .\mbtaCrTracker\getTrainInfo.py line direction
    return render_template('map.html')
