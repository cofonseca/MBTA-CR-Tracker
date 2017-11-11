from flask import Flask, render_template, request, url_for, redirect
from getTrainInfo import getTrainInfo
from lines import lines
app = Flask(__name__)

# Views
@app.route('/')
@app.route('/index')
def index():
    return render_template('search.html', lines=lines())

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

# Start The App
if __name__ == '__main__':
    app.run(debug=True)
