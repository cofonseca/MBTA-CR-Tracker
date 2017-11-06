from flask import Flask, render_template, request, url_for, redirect
from getTrainInfo import getTrainInfo

app = Flask(__name__)

# VIEWS

@app.route('/')
@app.route('/index')
def index():
    lines = [['Fairmount','Fairmount'],['Fitchburg','Fitchburg'],['Worcester','Framingham'],['Franklin','Franklin'],['Greenbush','Greenbush'],['Kingston','Kingston'],['Middleborough','Lakeville'],['Middleborough','Middleborough'],['Needham','Needham'],['Providence','Providence'],['Providence','Stoughton'],['Worcester','Worcester']]
    return render_template('index.html', lines=lines)

@app.route('/map', methods=['GET'])
def findTrain():
    line = request.args.get('line')
    direction = request.args.get('direction')
    coords = getTrainInfo(line, direction)
    app.logger.debug('Line: ' + line)
    app.logger.debug('Direction: ' + direction)
    return render_template('map.html', coords=coords)

@app.errorhandler(404)
def fourOhFour(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
    