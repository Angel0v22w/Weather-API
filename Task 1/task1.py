import requests
import random


API_KEY = "e21360b47c0180cd74537bf5a9427cb1"

# Списък с градове
CITIES = ["London", "Paris", "New York", "Tokyo", "Sydney"]

# Функция за извеждане на информация за времето
def get_weather_info(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    weather = data["weather"][0]["main"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    return weather, temperature, humidity

# Избор на 5 произволни града
random_cities = random.sample(CITIES, 5)

# Показване на информация за 5-те града
for city in random_cities:
    weather, temperature, humidity = get_weather_info(city)
    print(f"**{city}**")
    print(f"Време: {weather}")
    print(f"Температура: {temperature:.1f}°C")
    print(f"Влажност: {humidity}%")
    print()

# Изчисляване на статистики
min_temperature = float("inf")
total_temperature = 0

for city in random_cities:
    weather, temperature, humidity = get_weather_info(city)
    min_temperature = min(min_temperature, temperature)
    total_temperature += temperature

average_temperature = total_temperature / len(random_cities)

# Показване на статистики
print(f"Coldest city: {min_temperature:.1f}°C ({random_cities[int(min_temperature)]})")
print(f"Average temperature: {average_temperature:.1f}°C")

# Въвеждане на град от потребителя

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

