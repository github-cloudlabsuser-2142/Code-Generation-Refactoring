# Weather API Project

This project is a Python application that interacts with the OpenWeatherMap API to fetch weather data.

## Features

- Fetch current weather data for a specified location.
- Handle API responses and errors gracefully.
- Utility functions for data formatting.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd weather-api-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure your API key in `src/config/settings.py`.

## Usage

Run the main script to fetch weather data:
```
python src/weather_script.py
```

## Running Tests

To run the unit tests, use:
```
pytest tests/test_weather.py
```

## License

This project is licensed under the MIT License.