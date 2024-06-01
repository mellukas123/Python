import requests
from datetime import datetime, timedelta


def get_weather_forecast(latitude, longitude):
    # Define the API endpoint and parameters
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    }

    # Make the HTTP GET request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data:", response.status_code)
        return None


def print_weather_forecast(latitude, longitude):
    # Get the weather forecast data
    forecast_data = get_weather_forecast(latitude, longitude)

    if forecast_data:
        print("Weather forecast:")

        # Print current weather
        current_time = forecast_data['current']['time']
        current_temperature = forecast_data['current']['temperature_2m']
        current_wind_speed = forecast_data['current']['wind_speed_10m']
        print(f"Current time: {current_time}")
        print(f"Current temperature: {current_temperature}°C")
        print(f"Current wind speed: {current_wind_speed} m/s")

        # Print hourly forecast for the next 24 hours
        hourly_time = forecast_data['hourly']['time']
        hourly_temperature = forecast_data['hourly']['temperature_2m']
        hourly_relative_humidity = forecast_data['hourly']['relative_humidity_2m']
        hourly_wind_speed = forecast_data['hourly']['wind_speed_10m']

        print("\nHourly forecast for the next 24 hours:")
        for i in range(len(hourly_time)):
            print(f"Time: {hourly_time[i]}, Temperature: {hourly_temperature[i]}°C, "
                  f"Relative Humidity: {hourly_relative_humidity[i]}%, Wind Speed: {hourly_wind_speed[i]} m/s")
    else:
        print("Failed to fetch weather forecast.")


# Example usage
latitude = 52.52  # Latitude of Berlin
longitude = 13.41  # Longitude of Berlin
print_weather_forecast(latitude, longitude)
