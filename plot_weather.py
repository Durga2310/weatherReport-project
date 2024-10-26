# plot_weather.py

import matplotlib.pyplot as plt
from database_setup import Session, WeatherSummary


def plot_weather_trends():
    session = Session()
    results = session.query(WeatherSummary).all()

    dates = [result.date for result in results]
    temps = [result.temperature for result in results]
    cities = [result.city for result in results]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, temps, label="Temperature (Celsius)", marker='o')
    plt.xlabel("Date and Time")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature Trends Over Time")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
    session.close()


if __name__ == "__main__":
    plot_weather_trends()
