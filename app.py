from flask import Flask, render_template, request, url_for, redirect
from getTrainInfo import getTrainInfo
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
    app.logger.debug('Line: ' + line)
    app.logger.debug('Direction: ' + direction)
    trains = getAllTrainsMatchingCriteria(line, direction)

    if len(trains) == 0:
        app.logger.debug('No trains found matching criteria.')
        return render_template('search.html')
    elif len(trains) == 1:
        app.logger.debug('1 train matches the crieria.')
        coords = getTrainCoordinates(trains[0])
        return render_template('map.html', coords=coords)
    else:
        app.logger.debug('Multiple trains match the criteria.')
    return render_template('search.html')

@app.errorhandler(404)
def fourOhFour(error):
    return render_template('404.html'), 404

# Start The App
if __name__ == '__main__':
    app.run(debug=True)
