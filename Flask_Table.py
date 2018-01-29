from flask_table import Table, Col
import datetime

class ItemTable(Table):
    date = Col('Date')
    location = Col('Location')
    high_temp = Col('High Temperature')
    low_temp = Col('Low Temperature')
    precip_chance = Col('Precipitation Chance')
    summary = Col('Summary')


class Item(object):
    def __init__(self, date, location, high_temp, low_temp, precip_chance, summary):
        self.date = date
        self.location = location
        self.high_temp = high_temp
        self.low_temp = low_temp
        self.precip_chance = precip_chance
        self.summary = summary


def convert_num_to_date(num):
    now = datetime.datetime.now().date()
    future_date = str(now + datetime.timedelta(days=num))
    future_string = future_date.split('-')
    new_date = future_string[1] + '/' + future_string[2]
    return new_date


def create_flask_table(total_weather_data):
    day_forecasts = []
    for location_dict in total_weather_data:
        for day_num in sorted(location_dict):
            print(location_dict)
            date = convert_num_to_date(day_num)
            location = location_dict[day_num]['location'].capitalize()
            high_temp = location_dict[day_num]['high_temp']
            low_temp = location_dict[day_num]['low_temp']
            precip_chance = location_dict[day_num]['precipitation_chance']
            summary = location_dict[day_num]['summary']
            day_forecasts.append(Item(date, location, high_temp, low_temp, precip_chance, summary))
    return day_forecasts