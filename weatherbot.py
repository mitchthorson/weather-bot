import requests
import os
from models import Weather

forecast_api_key = os.environ.get("FORECAST_API_KEY", None)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the weather using our api key for the location specified by the lat/lng tuple
weather = Weather(forecast_api_key, ("38.9047", "-77.0164"))

with open("%s/output.txt" % current_dir, "w") as output:
    output.write(weather.get_weather_text())

