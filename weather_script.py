import requests
from datetime import datetime
import os
from dotenv import load_dotenv
import sys
from pathlib import Path

# Add src directory to path to allow imports
src_dir = Path(__file__).parent
root_dir = src_dir.parent
sys.path.append(str(root_dir))

# Load environment variables from root .env file
load_dotenv(root_dir / 'src' / '.env')

class WeatherAPI:
    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        if not self.api_key:
            raise ValueError("OPENWEATHER_API_KEY not found in environment variables")
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'  # For Celsius
            }
            
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            
            weather_data = response.json()
            return self._format_weather_data(weather_data)
            
        except requests.exceptions.RequestException as e:
            return f"Error fetching weather data: {e}"

    def _format_weather_data(self, data):
        return {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'timestamp': datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')
        }

def main():
    weather = WeatherAPI()
    while True:
        city = input("\nEnter city name (or 'quit' to exit): ")
        
        if city.lower() == 'quit':
            print("Goodbye!")
            break
            
        result = weather.get_weather(city)
        if isinstance(result, dict):
            print("\nWeather Information:")
            print(f"City: {result['city']}")
            print(f"Temperature: {result['temperature']}°C")
            print(f"Description: {result['description'].capitalize()}")
            print(f"Humidity: {result['humidity']}%")
            print(f"Wind Speed: {result['wind_speed']} m/s")
            print(f"Last Updated: {result['timestamp']}")
        else:
            print(result)

if __name__ == "__main__":
    main()