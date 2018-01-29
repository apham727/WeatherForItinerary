import forecastio

def getweather(latitude, longitude):
    location_weather_data = forecastio.load_forecast('9ef324d7369bc348c9111976ba66b71c', latitude, longitude)

    location_weather = {}
    count = 0
    for day_obj in location_weather_data.daily().data:
        location_weather[count] = {}
        location_weather[count]['high_temp'] = str(int(day_obj.apparentTemperatureHigh)) + '°'
        location_weather[count]['low_temp'] = str(int(day_obj.apparentTemperatureLow)) + '°'
        location_weather[count]['summary'] = day_obj.summary
        location_weather[count]['precipitation_chance'] = str(int(day_obj.precipProbability*100)) + '%'
        count += 1

    return location_weather