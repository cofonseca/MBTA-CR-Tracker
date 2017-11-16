from flask import Flask, render_template, request, url_for, redirect
from trainInfo import *
from lines import lines
app = Flask(__name__)


# Routes
@app.route('/')
@app.route('/index')
def index():
    return render_template('search.html', lines=lines())


@app.route('/trains', methods=['GET'])
def findTrainById():
    trainId = request.args.get('trainId')
    line = request.referrer.split('line=')[1].split('&')[0]
    app.logger.debug('Line: ' + line)
    direction = request.referrer.split('direction=')[1]
    app.logger.debug('Direction: ' + direction)
    app.logger.debug('Train ID: ' + trainId)
    url = request.url
    app.logger.debug('URL: ' + url)

    train = getAllTrainsMatchingCriteria(line, direction, trainId)
    coords = getTrainCoordinates(train)
    return render_template('map.html', coords=coords)


@app.route('/trains/find', methods=['GET'])
def findTrain():
    line = request.args.get('line')
    app.logger.debug('Line: ' + line)

    direction = request.args.get('direction')
    app.logger.debug('Direction: ' + direction)

    trains = getAllTrainsMatchingCriteria(line, direction, '000')

    if not trains:
        app.logger.debug('No trains found matching criteria.')
        return render_template('search.html')
        # flash that there aren't any trains running.
    elif len(trains) == 1:
        app.logger.debug('1 train matches the crieria.')
        coords = getTrainCoordinates(trains[0])
        return render_template('map.html', coords=coords)
    else:
        app.logger.debug('Multiple trains match the criteria.')
        return render_template('results.html', trainCount=len(trains), trains=trains)


@app.errorhandler(404)
def fourOhFour(error):
    return render_template('404.html'), 404


# Start The App
if __name__ == '__main__':
    app.run(debug=True)
