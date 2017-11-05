import requests

# COMMUTER RAIL LINE CODES
# Providence
# Worcester
# Fairmount
# Greenbush
# Middleborough
# Fitchburg
# Needham
# Kingston
# Newburyport
# Franklin
# Lowell

def getRoute():
    route = input('Enter Route ID:')
    return route

def getDirection():
    direction = input('Inbound or Outbound?')
    return direction

def getRouteInfoByRoute():
    # Gather Info and Make API Call
    route = getRoute()
    direction = getDirection()
    url = 'http://realtime.mbta.com/developer/api/v2/vehiclesbyroute?api_key=wX9NwuHnZU2ToO7GmGR9uw&route=CR-'+route+'&format=json'
    response = (requests.get(url)).json()
    # Return JSON Object
    for trip in response['direction']:
        if trip['direction_name'] == direction:
            return trip

def getVehicleCoordinates():
    latitude = routeInfo['trip'][0]['vehicle']['vehicle_lat']
    longitude = routeInfo['trip'][0]['vehicle']['vehicle_lon']
    return latitude+','+longitude

routeInfo = getRouteInfoByRoute()
coordinates = getVehicleCoordinates()
