import datetime
import requests

class Weather():
    
    email_output = "Hello, Right now it is %s and the date is %s. The current temperature is %s and today will have a high of %s."
    
    email_output_precip = email_output + " There is a %s percent chance of %s"

    def __init__(self, api_key, lat_lng):
        self.get_weather_data(api_key, lat_lng)

    def set_data(self, weather_data):
        self.current_temp = weather_data["currently"]["temperature"]
        self.current_precip_chance = weather_data["currently"]["precipProbability"]
        if self.current_precip_chance > 0:
            self.current_precip_type = weather_data["curently"]["precipType"]

        self.current_date = datetime.datetime.fromtimestamp(weather_data["currently"]["time"]).strftime('%m-%d-%Y')
        self.current_time = datetime.datetime.fromtimestamp(weather_data["currently"]["time"]).strftime('%H:%M')

        self.str_current_temp = str(int(self.current_temp)) + " degrees"

        self.today_high_temp = weather_data["daily"]["data"][0]["temperatureMax"]
        self.str_today_high = str(int(self.today_high_temp)) + " degrees"

    def get_weather_text(self):
        if self.current_precip_chance > 0:
            precip_percent = int(self.current_precip_chance * 100)
            return self.email_output_precip % (self.current_time, self.current_date, self.str_current_temp, self.str_today_high, precip_percent, self.current_precip_type)
        else:
            return self.email_output % (self.current_time, self.current_date, self.str_current_temp, self.str_today_high)
    
    def get_weather_data(self, api_key, lat_lng):
        forecast_api_url = "https://api.forecast.io/forecast/%s/%s,%s" % (api_key, lat_lng[0], lat_lng[1])
        r = requests.get(forecast_api_url)
        while r.status_code is not 200:
            print "Error getting data, check that URL!"
            break
        self.set_data(r.json())
