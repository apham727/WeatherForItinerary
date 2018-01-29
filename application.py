from flask import Flask, render_template, request
from getdata import get_weather_data
from parseweatherdata import parse_weather_data
import Flask_Table

app = Flask(__name__)

total_weather_data = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/addlocation', methods = ['POST'])
def add_another():
    global total_weather_data
    location = request.form['location']
    location_start = request.form['start_date']
    location_end = request.form['end_date']

    all_location_weather_data = get_weather_data(location)
    location_weather_data = parse_weather_data(all_location_weather_data, location_start, location_end)
    for day_num in location_weather_data:
        location_weather_data[day_num]['location'] = location
    total_weather_data.append(location_weather_data)
    return render_template('addanother.html')

@app.route('/addanother', methods=['POST'])
def create_forecast():
    global total_weather_data
    if 'submit' in request.form.values():
        items = Flask_Table.create_flask_table(total_weather_data)
        table = Flask_Table.ItemTable(items)
        return render_template('forecast.html', html_table = table)
    else:
        print('adding another location')
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)



