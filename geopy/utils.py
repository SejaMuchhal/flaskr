import requests
from os import environ

def get_geocode_response(address):
    url = environ.get('GEOCODE_API_URL')
    api_key = environ.get('GEOCODE_API_KEY')

    params = {'address':address, 'key': api_key}

    geocode_response = requests.get(url = url, params = params)

    data = geocode_response.json()
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    formatted_address = data['results'][0]['formatted_address']
    
    result_data = { "coordinates" : {'lat': latitude, 'lng':longitude}, "address": formatted_address}
    
    return result_data