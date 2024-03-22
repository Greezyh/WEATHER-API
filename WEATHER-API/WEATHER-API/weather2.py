import requests

def get_weather(city_name):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=api_key.txt&units=metric'
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"Current weather in {city_name}: {temperature}°C, {description}")
    else:
        print(f"Failed to fetch weather data for {city_name}")

city_name = input('Enter city name: ')
get_weather(city_name)
