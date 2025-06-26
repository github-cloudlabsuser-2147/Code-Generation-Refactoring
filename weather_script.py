# Fetch weather data from OpenWeatherMap API
import requests

key = "cbea73fa53f0dd054f1b8c70bde24472"

def fetch_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data.get('main', {})
        weather = data.get('weather', [{}])[0]
        temp = main.get('temp')
        description = weather.get('description')
        return f"Weather in {city}: {temp}°C, {description}"
    else:
        return f"Failed to fetch weather data for {city}."

print ( fetch_weather("London", key))
print (fetch_weather("New York", key))