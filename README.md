# Weather Monitoring Project

This Python project monitors real-time weather conditions for various cities in India using the OpenWeatherMap API. It fetches weather data at regular intervals (every 5 minutes), processes it, and stores it in a SQLite database. The project is configured to retrieve data for the following cities: Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad.

## Features

- Fetches real-time weather data, including temperature and weather conditions.
- Converts temperature from Kelvin to Celsius.
- Stores weather data with timestamped entries for each city.
- Configurable scheduling to run every 5 minutes using the `schedule` library.

## Project Structure

- **weather_data.py**: Main script that fetches and stores weather data.
- **database_setup.py**: Script for setting up the SQLite database and defining the `WeatherSummary` model.
- **get_weather_data.py**: Contains the `get_weather_data()` function to retrieve weather data from OpenWeatherMap.
- **requirements.txt**: Lists project dependencies.
- **README.md**: Project description and setup instructions (this file).

## Requirements

- Python 3.7+
- [OpenWeatherMap API Key](https://openweathermap.org/) (free API key required)
- Required Python packages (see `requirements.txt`):
  - `requests`
  - `schedule`
  - `SQLAlchemy`

## Setup Instructions

1. **Clone or Extract the Project**  
   Clone this repository or extract the ZIP file you have.

2. **Install Dependencies**  
   Use the following command to install the required packages:

   ```bash
   pip install -r requirements.txt
