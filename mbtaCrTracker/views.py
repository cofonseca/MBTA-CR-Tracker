from flask import render_template, request, redirect
from mbtaCrTracker import app
from getTrainInfo import getTrainInfo
#import sys

@app.route('/')
@app.route('/index')
def index():
    lines = [['Fairmount','Fairmount'],['Fitchburg','Fitchburg'],['Worcester','Framingham'],['Franklin','Franklin'],['Greenbush','Greenbush'],['Kingston','Kingston'],['Middleborough','Lakevile'],['Middleborough','Middleborough'],['Needham','Needham'],['Providence','Providence'],['Providence','Stoughton'],['Worcester','Worcester']]
    return render_template('index.html', lines=lines)

@app.route('/map', methods=['GET'])
def findTrain():
    line = request.args.get('line')
    direction = request.args.get('direction')
    coords = getTrainInfo(line,direction)
    app.logger.debug('Line: ' + line)
    app.logger.debug('Direction: ' + direction)
    return render_template('map.html', coords=coords)

@app.errorhandler(404)
def fourohfour():
    return render_template('404.html')