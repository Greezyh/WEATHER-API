import requests
import json
from datetime import datetime, timedelta
import csv

# Constants
API_KEY = 'api_key.txt'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
HISTORICAL_URL = 'https://api.openweathermap.org/data/2.5/onecall/timemachine'
UNITS = 'metric'

# Function to get current weather data for a city
def get_current_weather(city):
    params = {
        'q': city,
        'units': UNITS,
        'appid': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

# Function to get historical weather data for a city on a specific date
def get_historical_weather(city, date):
    timestamp = int(datetime.strptime(date, '%Y-%m-%d').timestamp())
    params = {
        'lat': 0,  # Use lat/lon of the city
        'lon': 0,  # Use lat/lon of the city
        'dt': timestamp,
        'units': UNITS,
        'appid': API_KEY
    }
    response = requests.get(HISTORICAL_URL, params=params)
    return response.json()

# Function to calculate average, median, and mode of temperatures
def calculate_statistics(temps):
    avg_temp = sum(temps) / len(temps)
    median_temp = sorted(temps)[len(temps) // 2]
    mode_temp = max(set(temps), key=temps.count)
    return avg_temp, median_temp, mode_temp

# Function to save weather data to a file
def save_to_file(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Temperature'])
        for date, temp in data.items():
            writer.writerow([date, temp])

if __name__ == '__main__':
    # User input for city name and date
    city = input('Enter city name: ')
    current_weather = get_current_weather(city)
    try:
        # Try to access the temperature data
        temp = current_weather['main']['temp']
        print(f"Current weather in {city}: {temp}°C")
    except KeyError:
        # Handle the KeyError gracefully
        print(f"Could not retrieve weather data for {city}. Please check the city name.")

    historical_date = input('Enter date for historical weather (YYYY-MM-DD): ')
    historical_weather = get_historical_weather(city, historical_date)
    temperatures = [entry['temp'] for entry in historical_weather['hourly']]
    avg_temp, median_temp, mode_temp = calculate_statistics(temperatures)
    print(f"Average temperature: {avg_temp}°C")
    print(f"Median temperature: {median_temp}°C")
    print(f"Mode temperature: {mode_temp}°C")

    # Save historical weather data to a file
    save_to_file('weather_data.csv', historical_weather)
