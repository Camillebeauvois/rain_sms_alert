import os
from twilio.rest import Client
import requests

MY_LAT = 13.756331
MY_LONG = 100.501762

API_KEY = os.environ.get('api_key')
ACCOUNT_SID = os.environ.get('account_sid')
TOKEN = os.environ.get('token')
MY_PHONE = os.environ.get('my_phone')

hourly_endpoint = "https://api.openweathermap.org/data/3.0/onecall"

params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts"
}

weather_data = requests.get(url=hourly_endpoint, params=params).json()
weather_today = weather_data["hourly"][0:12]

will_rain = False
for hour in weather_today:
    id = hour["weather"][0]["id"]
    if id > 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, TOKEN)
    message = client.messages.create(
                         body="Bring an umbrella ☔️",
                         from_='+16206341787',
                         to=MY_PHONE
                     )
