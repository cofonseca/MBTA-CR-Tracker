import requests
import sys

def getRouteInfo(line, direction):
    # Gather Info and Make API Call
    #route = getRoute()
    #direction = getDirection()
    url = 'http://realtime.mbta.com/developer/api/v2/vehiclesbyroute?api_key=wX9NwuHnZU2ToO7GmGR9uw&route=CR-'+line+'&format=json'
    response = (requests.get(url)).json()
    # Return JSON Object
    for trip in response['direction']:
        if trip['direction_name'] == direction:
            return trip

def getVehicleCoordinates():
    latitude = routeInfo['trip'][0]['vehicle']['vehicle_lat']
    longitude = routeInfo['trip'][0]['vehicle']['vehicle_lon']
    return latitude+','+longitude

routeInfo = getRouteInfo(sys.argv[1], sys.argv[2])
coordinates = getVehicleCoordinates()

print(coordinates)
