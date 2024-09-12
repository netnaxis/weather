import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime, timezone

API_KEY = 'your_api_key'  # Replace with your API key
CITY = 'Kyiv'
API_URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

def fetch_weather_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise exception for any 4xx/5xx responses
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the API: {e}")
        return None

def save_weather_data(weather_data):
    filename = 'weather_data.json'
    with open(filename, 'w') as json_file:
        json.dump(weather_data, json_file, indent=4)
    print(f"Weather data saved to {filename}")

def plot_weather_data(weather_data):
    dates = []
    temperatures = []
    
    for entry in weather_data['list']:
        timestamp = entry['dt']
        temperature = entry['main']['temp']
        date = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime('%m-%d %H:%M')
        dates.append(date)
        temperatures.append(temperature)
    
    plt.figure(figsize=(10, 5))
    plt.plot(dates, temperatures, marker='o')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Date-Time (MM-DD)')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Temperature Forecast for {weather_data["city"]["name"]}')
    plt.tight_layout()
    plt.show()

def main():
    # Step 1: Fetch data from the API
    weather_data = fetch_weather_data()
    
    if weather_data:
        # Step 2: Save the data to a JSON file
        save_weather_data(weather_data)
        
        # Step 3: Visualize the data
        plot_weather_data(weather_data)

if __name__ == '__main__':
    main()
