import requests
import pandas as pd
import random
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('API_KEY')
cities = pd.read_csv('worldcities.csv')
CITIES = cities['city']




def city_weather():
    '''This fucntion takes 5 random cities from the worldcities.csv file and sends them to the weather platform 
        and receives information about the weather for these five cities.'''
    counter = 0
    all_cities = {}
    total_temp = 0
    #checking for every city if it exist in the weather platform if it doesnt removes the city from the csv file 
    #until it finds 5 valid cities.
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

    
      
    # Get the min temp for all five cities
    min_temp = 1000
    coldest_city = ''
    for k,v in all_cities.items():
        current_temp = v[1]
        if current_temp < min_temp:
            min_temp = current_temp
            coldest_city = k

    # Get the average temp for all five cities
    average_temperature = total_temp / 5
    average_temperature = round(average_temperature,1)

    return all_cities, min_temp, average_temperature, coldest_city

def get_another_city(city):
    '''This function gets a specific city weather'''
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    print(f'City: {city} has {response.status_code} code.')
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["main"]
        temperature = float(data["main"]["temp"])
        humidity = data["main"]["humidity"]
        counter += 1
    else:
        print(f"City: {city} doesnt exist in the database. Try anohter.")
    return weather, temperature, humidity


   


all_cities, min_temp, average_temperature, coldest_city = city_weather()
for city, values in all_cities.items():
    print(f'City: {city}')
    print(f'Weather: {values[0]}')
    print(f'Temperture: {values[1]} °C')
    print(f'Humidity: {values[2]} %')

print(f"Coldest city: {min_temp:.1f}°C ({coldest_city(min_temp)})")
print(f"Average temperature: {average_temperature:.1f}°C")



question = input('Do you want the weather for another city? y/n \n').lower()

if question == 'y':
    city = input("Въведете град: ")
    weather, temperature, humidity = get_another_city(city)

    print(f"**{city}**")
    print(f"Време: {weather}")
    print(f"Температура: {temperature:.1f} °C")
    print(f"Влажност: {humidity} %")

    
        






