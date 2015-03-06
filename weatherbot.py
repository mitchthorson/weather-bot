import requests
import datetime
import json
import os

email_output = "Hello, Right now it is %s and the date is %s. The current temperature is %s and today will have a high of %s."
forecast_api_key = os.environ.get("FORECAST_API_KEY", None)
current_dir = os.path.dirname(os.path.abspath(__file__))

def get_weather_data(api_key, lat, lng):
    forecast_api_url = "https://api.forecast.io/forecast/%s/%s,%s" % (api_key, lat, lng)
    r = requests.get(forecast_api_url)
    while r.status_code is not 200:
        print "Error getting data, check that URL!"
        break
    return r.json()

weather_data = get_weather_data(forecast_api_key, "38.9047", "-77.0164")

current_temp = weather_data["currently"]["temperature"]
current_precip_chance = weather_data["currently"]["precipProbability"]
if current_precip_chance > 0:
    current_precip_type = weather_data["curently"]["precipType"]

current_date = datetime.datetime.fromtimestamp(weather_data["currently"]["time"]).strftime('%m-%d-%Y')
current_time = datetime.datetime.fromtimestamp(weather_data["currently"]["time"]).strftime('%H:%M')

str_current_temp = str(int(current_temp)) + " degrees"

today_high_temp = weather_data["daily"]["data"][0]["temperatureMax"]
str_today_high = str(int(today_high_temp)) + " degrees"

todays_weather_text = email_output % (current_time, current_date, str_current_temp, str_today_high)

with open("%s/output.txt" % current_dir, "w") as output:
    output.write(todays_weather_text)

