import datetime

def parse_weather_data(weather_data, location_start, location_end):
    start_index = num_days_from_now(location_start)
    end_index = num_days_from_now(location_end)
    day_range = range(start_index,end_index+1)
    parsed_data = {}
    for day_num,day_weather in weather_data.items():
        if day_num in day_range:
            parsed_data[day_num] = day_weather
    return parsed_data


def num_days_from_now(future_date):
    now = datetime.datetime.now().date()
    future_string = future_date.split('-')
    future = datetime.date(int(future_string[0]), int(future_string[1]), int(future_string[2]))
    return abs((future-now).days)




