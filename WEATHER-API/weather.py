import datetime as dt
import requests

# Base URL for the OpenWeatherMap API
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'

# Read the API key from a text file (api_key.txt)
API_KEY = open('api_key.txt', 'r').read().strip()

# City for which weather data will be retrieved
CITY = 'Pretoria'

# Function to convert temperature in Kelvin to Celsius and Fahrenheit
def kelvin_to_celcius_farenheit(kelvin):
    celcius = kelvin - 273.15
    farenheit = celcius * 9/5 + 32
    return celcius, farenheit

# Construct the URL for the API request
url = BASE_URL + 'q=' + CITY + '&appid=' + API_KEY

# Make a GET request to the API and convert the response to JSON
response = requests.get(url).json()

# Extract relevant weather data from the API response
temp_kelvin = response['main']['temp']
temp_celcius, temp_farenheit = kelvin_to_celcius_farenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celcius, feels_like_farenheit = kelvin_to_celcius_farenheit(feels_like_kelvin)
humidity = response['main']['humidity']
wind_speed = response['wind']['speed']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone']).strftime('%Y-%m-%d %H:%M:%S')
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone']).strftime('%Y-%m-%d %H:%M:%S')

# Print the weather data
print(f'Temperature in {CITY}: {temp_celcius:.2f}°C or {temp_farenheit:.2f}°F')
print(f'Feels like temperature in {CITY}: {feels_like_celcius:.2f}°C or {feels_like_farenheit:.2f}°F')
print(f'Humidity in {CITY}: {humidity}%')
print(f'Wind Speed in {CITY}: {wind_speed} m/s')
print(f'General weather in {CITY}: {description}')
print(f'Sun rises in {CITY} at {sunrise_time} local time')
print(f'Sun sets in {CITY} at {sunset_time} local time')
