import requests
import pandas as pd
import random
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('API_KEY')
cities = pd.read_csv('worldcities.csv')


CITIES = cities['city']


def get_weather_info(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    weather = data["weather"][0]["main"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    return weather, temperature, humidity


random_cities = random.sample(CITIES.tolist(), 5)


for city in random_cities:
    weather, temperature, humidity = get_weather_info(city)
    print(f"**{city}**")
    print(f"Време: {weather}")
    print(f"Температура: {temperature:.1f}°C")
    print(f"Влажност: {humidity}%")
    print()

def find_city(min_temp):
    for key, value in all_temp.items():
        if value == min_temp:
            return key


total_temperature = 0
all_temp = {}

for city in random_cities:
    weather, temperature, humidity = get_weather_info(city)
    all_temp[city] = temperature
    total_temperature += temperature

average_temperature = total_temperature / len(random_cities)
min_temp = min(all_temp.values())

print(f"Coldest city: {min_temp:.1f}°C ({find_city(min_temp)})")
print(f"Average temperature: {average_temperature:.1f}°C")

question = input('Do you want the weather for another city? y/n \n').lower()

if question == 'y':

    while True:
        city = input("Въведете град: ")
        weather, temperature, humidity = get_weather_info(city)

        print(f"**{city}**")
        print(f"Време: {weather}")
        print(f"Температура: {temperature:.1f}°C")
        print(f"Влажност: {humidity}%")
        break






