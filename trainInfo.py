import requests
import sys

def getTrainInfo(line, direction):

    def getAllTrainsMatchingCriteria(line, direction):
        # Returns a list of all trains that meet the user's search criteria.
        print('Search Criteria: ' + line + ' ' + direction)
        
        # Make API Call
        url = 'http://realtime.mbta.com/developer/api/v2/vehiclesbyroute?api_key=DXxEHBSTPEKF4sFlsamMaw&route=CR-'+line+'&format=json'
        try:
            response = (requests.get(url)).json()
        except:
            print('Unable to connect to API endpoint at realtime.mbta.com')
        
        # Parse Data
        for trip in response['direction']:
            if trip['direction_name'] == direction:
                trains = []
                for train in trip['trip']:
                    trains.append(train)
                    print('\nFound Train:')
                    print(train)
                print('Found ' + len(trains) + ' train(s) matching the search criteria.')
                return trains

    def getTrainCoordinates(train):
        # Takes a train object from getAllTrainsMatchingCriteria(), and returns its coordinates
        lat = train['vehicle']['vehicle_lat']
        lon = train['vehicle']['vehicle_lon']
        return lat,lon

    trains = getAllTrainsMatchingCriteria(line, direction)