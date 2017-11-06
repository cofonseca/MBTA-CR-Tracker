import requests
import sys

def getTrainInfo(line, direction):

    def getRouteInfo(line, direction):
        url = 'http://realtime.mbta.com/developer/api/v2/vehiclesbyroute?api_key=wX9NwuHnZU2ToO7GmGR9uw&route=CR-'+line+'&format=json'
        response = (requests.get(url)).json()
        # Return JSON Object
        for trip in response['direction']:
            if trip['direction_name'] == direction:
                return trip

    def getVehicleCoordinates():
        latitude = routeInfo['trip'][0]['vehicle']['vehicle_lat']
        longitude = routeInfo['trip'][0]['vehicle']['vehicle_lon']
        return latitude,longitude

    routeInfo = getRouteInfo(line, direction)
    if routeInfo:
        coordinates = getVehicleCoordinates()
        return coordinates
    else:
        print('No ' + direction + ' trains are currently running on the ' + line + ' line.')
