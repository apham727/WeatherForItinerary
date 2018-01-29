import googlemaps
from darkskyforecast import getweather

def get_weather_data(location):
    gm_output = googlemaps.Client(key='AIzaSyDE_hyflEm38XOWXi1mzfGxULfa9PWdV6o').geocode(location)

    latitude = gm_output[0]['geometry']['location']['lat']
    longitude = gm_output[0]['geometry']['location']['lng']

    location_weather = getweather(latitude,longitude)
    return location_weather


