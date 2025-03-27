import requests

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather_data(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use metric units for temperature in Celsius
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

# Function to process and display weather data
def display_weather_info(weather_data):
    if weather_data:
        city = weather_data.get("name")
        main = weather_data.get("main", {})
        weather = weather_data.get("weather", [{}])[0]

        temperature = main.get("temp")
        humidity = main.get("humidity")
        condition = weather.get("description")

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition.capitalize()}")
    else:
        print("No weather data to display.")

# Example usage
if __name__ == "__main__":
    API_KEY = "your_openweathermap_api_key"  # Replace with your OpenWeatherMap API key
    CITY = "London"  # Replace with the desired city

    weather_data = fetch_weather_data(API_KEY, CITY)
    display_weather_info(weather_data)