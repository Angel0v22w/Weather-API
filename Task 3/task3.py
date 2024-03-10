from flask import Flask,render_template,request
import pandas as pd
import random
import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.environ.get('API_KEY')
cities = pd.read_csv('worldcities.csv')
CITIES = cities['city']




app = Flask(__name__)


def city_weather():
    '''This fucntion does something.'''
    counter = 0
    all_cities = {}
    total_temp = 0
    while counter != 5:
        random_city = random.sample(CITIES.tolist(), 1)
        random_city = random_city[0]
        url = f"https://api.openweathermap.org/data/2.5/weather?q={random_city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        print(f'City: {random_city} has {response.status_code} code.')
        if response.status_code == 200:
            data = response.json()
            weather = data["weather"][0]["main"]
            temperature = float(data["main"]["temp"])
            humidity = data["main"]["humidity"]
            all_cities[random_city] = [weather, temperature, humidity]
            total_temp += temperature
            counter += 1
        else:
            # Read the CSV file into a DataFrame
            df = pd.read_csv("worldcities.csv")
            df = df.drop(df[df['city'] == random_city].index)
            print(f"City: {random_city} has been removed.")
            continue
      
    min_temp = 1000
    coldest_city = ''
    for k,v in all_cities.items():
        # Get the min temp for all five cities
        current_temp = v[1]
        if current_temp < min_temp:
            min_temp = current_temp
            coldest_city = k

        # Get the average temp for all five cities
    average_temperature = total_temp / 5
    average_temperature = round(average_temperature,1)

    return all_cities, min_temp, average_temperature, coldest_city


@app.route('/')
def test():
    all_city, min_temp, average_temperature, coldest_city = city_weather()

    return render_template('test.html', lines = all_city, min_temp=min_temp, average_temperature=average_temperature, coldest_city=coldest_city)   
  
@app.route("/submit", methods=["POST"])
def submit():
    city = request.form.get('city')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    weather = data["weather"][0]["main"]
    temperature = float(data["main"]["temp"])
    humidity = data["main"]["humidity"]

    return render_template('test.html', new_city=city, weather = weather, temperature=temperature, humidity=humidity )



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)



# {% if data[0] == 'Clear' %}
# <span class="icon"><img class="img-fluid" src="https://img.icons8.com/emoji/96/000000/sun-emoji.png"/></span>
# {% elif data[0] == 'Clouds' %}
#     <span class="icon"><img class="img-fluid" src="https://img.icons8.com/office/80/000000/partly-cloudy-day.png"/></span>
# {% elif data[0] == 'Rain' %}
#     <span class="icon"><img class="img-fluid" src='../static/img/rain.png'/></span>
# {% elif data[0] == 'Mist' %}
#     <span class="icon"><img class="img-fluid" src='../static/img/mist.png'/></span>
# {% endif %}