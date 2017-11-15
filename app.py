from flask import Flask, render_template, request, url_for, redirect
from trainInfo import *
from lines import lines
app = Flask(__name__)

# Views
@app.route('/')
@app.route('/index')
def index():
    return render_template('search.html', lines=lines())

@app.route('/trains/find', methods=['GET'])
def findTrain():
    line = request.args.get('line')
    direction = request.args.get('direction')
    trainId = request.args.get('trainId')
    if line:
        app.logger.debug('Line: ' + line)
    if direction:
        app.logger.debug('Direction: ' + direction)

    if trainId:
        app.logger.debug('Trip ID: ' + trainId)
        trains = getAllTrainsMatchingCriteria(line, direction, trainId)
    else:
        trains = getAllTrainsMatchingCriteria(line, direction, 0)
        
    trainCount = len(trains)

    if trainCount == 0:
        app.logger.debug('No trains found matching criteria.')
        return render_template('search.html')
    elif trainCount == 1:
        app.logger.debug('1 train matches the crieria.')
        coords = getTrainCoordinates(trains[0])
        return render_template('map.html', coords=coords)
    else:
        app.logger.debug('Multiple trains match the criteria.')
        return render_template('results.html', trainCount=trainCount, trains=trains, line=line, direction=direction)

@app.errorhandler(404)
def fourOhFour(error):
    return render_template('404.html'), 404

# Start The App
if __name__ == '__main__':
    app.run(debug=True)
