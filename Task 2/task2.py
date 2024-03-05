import tkinter as tk
from tkinter import ttk
import requests
import requests
import random
import os
from dotenv import load_dotenv



load_dotenv()

API_KEY = os.environ.get('API_KEY')


CITIES = ["Tokyo", "Delhi", "Shanghai", "São Paulo", "Mexico City", "New York City", 
          "Cairo", "Buenos Aires", "Dhaka", "Moscow", "Lagos", "London", 
          "Istanbul", "Paris", "Seoul", "Osaka", "Rio de Janeiro", "Los Angeles", 
          "Beijing", "Karachi", "Bogotá", "Johannesburg", "Chennai", "Jakarta", 
          "Bangkok", "Berlin", "Toronto", "Rome", "Sydney", "Madrid"]


def get_weather_info(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    weather = data["weather"][0]["main"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    return weather, temperature, humidity


random_cities = random.sample(CITIES, 5)

def find_city(min_temp,all_temp):
    for key, value in all_temp.items():
        if value == min_temp:
            return key
    
    
def update_info():
    total_temperature = 0
    all_temp = {}
    for city in random_cities:
        weather, temp, humidity = get_weather_info(city)
        all_temp[city] = temp
        total_temperature += temp
        tfield.insert(tk.INSERT,f"Град {city}\n Време {weather}\n Температура {temp:.1f}°C\n Влажност {humidity}\n --------------\n")
    
    min_temp = min(all_temp.values())
    average_temperature = total_temperature / len(random_cities)
    tfield.insert(tk.INSERT,f"Coldest city: {min_temp:.1f}°C ({find_city(min_temp,all_temp)})\n")
    tfield.insert(tk.INSERT,f"Average temperature: {average_temperature:.1f}°C")

def info(city):
    weather, temp, humidity = get_weather_info(city)
    tfield.insert(tk.INSERT,f"Град {city}\n Време {weather}\n Температура {temp}\n Влажност {humidity}\n")

window = tk.Tk()
window.title("Прогноза за времето")

main_frame = tk.Frame(window)
search_frame = tk.Frame(window)
search_entry = tk.Entry(search_frame)
search_button = tk.Button(search_frame, text="Търсене", command=lambda: info(search_entry.get()))



main_frame.pack()
search_frame.pack()
tfield = tk.Text(main_frame, width=46, height=10)
tfield.pack()
search_entry.pack(side=tk.LEFT)
search_button.pack(side=tk.LEFT)

update_info()

window.mainloop()











