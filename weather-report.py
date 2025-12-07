import requests
import json
import datetime

def get_weather(region):
    """Fetches weather data for a given region using OpenWeatherMap API and formats a weather report.

    Args:
        region: The city name or zip code for which to retrieve weather data.

    Returns:
        A string containing a formatted weather report with time, or an error message if data retrieval fails.
    """
    api_key = "19c28f745b8ada44ab38a85f5d477edd"  # Replace with your actual OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={region}&appid={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        temp = data["main"]["temp"] - 273.15  # Convert Kelvin to Celsius
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        sunset = data["sys"]["sunset"]  # Sunset time in seconds since epoch

        # Estimate dusk (around sunset + civil twilight duration)
        dusk = datetime.datetime.utcfromtimestamp(sunset) + datetime.timedelta(minutes=75)  # Adjust offset based on your location

        # Get current time
        current_time = datetime.datetime.now().strftime('%H:%M:%S')

        # Format weather report
        report = f"*Weather Report for {data['name']}, {region}*\n"
        report += f"* Time: {current_time}\n"
        report += f"* Temperature: {temp:.2f}°C\n"
        report += f"* Humidity: {humidity}%\n"
        report += f"* Weather: {weather}\n"
        report += f"* Estimated Dusk: {dusk.strftime('%H:%M')}\n"
        return report
    else:
        return f"Error: Could not retrieve weather data ({response.status_code})"

# Get user input
region = input("Enter a city name or zip code: ")

# Get and display weather report
weather_info = get_weather(region)
print(weather_info)
