from flask import Flask,render_template
import pandas as pd
import random
import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.environ.get('API_KEY')
cities = pd.read_csv('worldcities.csv')
CITIES = cities['city']


def get_weather_info(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    print(response)
    data = response.json()
    

    weather = data["weather"][0]["main"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    return weather, temperature, humidity

def find_city(min_temp,all_temp):
    for key, value in all_temp.items():
        if value == min_temp:
            return key
    
        
def update_info():
    random_cities = random.sample(CITIES.tolist(), 5)
    total_temperature = 0
    all_temp = {}
    all_city = {}
    for city in random_cities:
        weather, temp, humidity = get_weather_info(city)
        all_temp[city] = temp
        all_city[city] = [weather,temp,humidity]
        total_temperature += temp

    min_temp = min(all_temp.values())
    coldest_city = find_city(min_temp,all_temp)
    average_temperature = total_temperature / len(random_cities)
    return all_city,min_temp,average_temperature,coldest_city


app = Flask(__name__)

@app.route('/')

def hello():
    all_city, min_temp, average_temperature, coldest_city = update_info()
    return render_template('index.html',lines = all_city)   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)