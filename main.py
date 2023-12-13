#From Open Weather API
from keys import *

import requests

weather_params = {
    "lat": my_lat,
    "lon" :my_long,
    "appid": api_key,
    "cnt": 4
}

response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=weather_params)
response.raise_for_status()
status = response.status_code
weather_data = response.json()
print(f"Status code: {status}")
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    conditon_code = hour_data["weather"][0]["id"]
    if int(conditon_code) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella.")
else:
    print("No need to worry about any rain or snow.")
