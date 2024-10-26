import requests
import schedule
import time
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from database_setup import WeatherSummary, engine  # Ensure this matches your setup

API_KEY = '6d61719239434a6c896791c8f1f68cf3'  # Replace with your OpenWeatherMap API key

# Set up the database session
Session = sessionmaker(bind=engine)

# List of cities in India to fetch weather data for
cities = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(temp_kelvin):
    return temp_kelvin - 273.15

# Function to fetch and store weather data for a city
def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        # Parse response JSON data
        data = response.json()

        # Extract main temperature data
        temp_kelvin = data['main']['temp']
        temp_celsius = kelvin_to_celsius(temp_kelvin)
        weather_condition = data['weather'][0]['main']

        # Store data in the database
        session = Session()
        weather_summary = WeatherSummary(
            city=city,
            temperature=temp_celsius,
            weather_condition=weather_condition,
            date=datetime.now()
        )
        session.add(weather_summary)
        session.commit()
        session.close()

        print(f"Data for {city} stored in the database.")
    else:
        # Print error message if the request fails
        print(f"Failed to fetch data for {city}. Status Code: {response.status_code}")
        print("Response:", response.text)

# Function to fetch and store data for all cities
def fetch_and_store_weather_data():
    for city in cities:
        get_weather_data(city)

# Schedule the task to run every 5 minutes
schedule.every(5).minutes.do(fetch_and_store_weather_data)

# Keep the script running to allow scheduled tasks to run
if __name__ == "__main__":
    print("Starting the weather data fetch every 5 minutes...")
    while True:
        schedule.run_pending()
        time.sleep(1)  # Wait 1 second between checks
