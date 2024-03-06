import datetime as dt
import requests

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
API_KEY = open('api_key.txt', 'r').read().strip()
CITY = 'Pretoria'

def kelvin_to_celcius_farenheit(kelvin):
    celcius = kelvin - 273.15
    farenheit = celcius * 9/5 + 32
    return celcius, farenheit

url = BASE_URL + 'q=' + CITY + '&appid=' + API_KEY
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celcius, temp_farenheit = kelvin_to_celcius_farenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celcius, feels_like_farenheit = kelvin_to_celcius_farenheit(feels_like_kelvin)
humidity = response['main']['humidity']
wind_speed = response['wind']['speed']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone']).strftime('%Y-%m-%d %H:%M:%S')
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone']).strftime('%Y-%m-%d %H:%M:%S')

print(f'Temperature in {CITY}: {temp_celcius:.2f}°C or {temp_farenheit:.2f}°F')
print(f'Feels like temperature in {CITY}: {feels_like_celcius:.2f}°C or {feels_like_farenheit:.2f}°F')
print(f'Humidity in {CITY}: {humidity}%')
print(f'Wind Speed in {CITY}: {wind_speed} m/s')
print(f'General weather in {CITY}: {description}')
print(f'Sun rises in {CITY} at {sunrise_time} local time')
print(f'Sun sets in {CITY} at {sunset_time} local time')