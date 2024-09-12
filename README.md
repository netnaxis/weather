# Weather Data Fetch and Visualization Script

This script fetches weather forecast data from the OpenWeatherMap API, processes it, saves it into a JSON file, and visualizes the temperature trends using Matplotlib.

## Features
- Fetches 5-day weather forecast data for a specified city from the OpenWeatherMap API.
- Saves the weather data into a `weather_data.json` file.
- Visualizes the temperature trends with a simple line chart.

## Prerequisites
- Python 3.x
- OpenWeatherMap API Key

## Getting Started

### 1. Clone the Repository
To get started, clone this repository to your local machine:
```bash
git clone https://github.com/netnaxis/weather.git
cd weather
```

### 2. Install Required Libraries
Use `pip` to install the required Python libraries:
```
pip install -r requirements.txt
```

### 3. Get OpenWeatherMap API Key
You need an API key from OpenWeatherMap to fetch weather data. Follow these steps:
1. Go to [OpenWeatherMap](https://openweathermap.org/) and sign up.
2. After logging in, go to the "API keys" section and generate a key.
3. Copy your API key and replace the placeholder `your_api_key` in the Python script (`weather.py`) with your actual API key.

### 4. Run the Script

To fetch weather data, save it to a file, and visualize the temperature trends, run the script as follows:

```
python weather.py
```

This will generate a temperature forecast chart for the next 5 days in the specified city.

## Modifying the City

By default, the script fetches the weather data for `Kyiv`. You can change the city by modifying the `CITY` variable in the script:

```
CITY = 'Your City Name'
```

### Output
- The fetched weather data will be saved in weather_data.json.
- A plot will be displayed showing the temperature trend for the next 5 days, with dates in the format MM-DD HH:MM.