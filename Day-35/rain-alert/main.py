import requests
from twilio.rest import Client
import os

api_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("apiKey")

parameters = {
    "lat":25.2697416265553,
    "lon":82.96507153849362,
    "exclude":"current,minutely,daily",
    "appid": api_key
}

response = requests.get(api_endpoint, params=parameters)
response.raise_for_status()
data = response.json()

id =  [data["hourly"][i]["weather"][0]["id"] for i in range(12)]

for num in id:
    if num < 700:
        print("It's going to rain")
        account_sid = os.environ.get("accountSID")
        auth_token = os.environ.get("authToken")
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body="It's going to rain",
                from_= os.environ.get("twilioNum"),
                to = os.environ.get("myNum")
            )
        print(message.status)
        break
else:
    print("It's not going to rain")