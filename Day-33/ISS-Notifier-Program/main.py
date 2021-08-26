import requests
from datetime import datetime
import smtplib
import time
import os

MY_LAT = 25.317644 
MY_LONG = 82.973915 
SUNRISE = 5
SUNSET = 18

MY_EMAIL = os.environ['MY_EMAIL']
PASS = os.environ['PASS']


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

def is_iss_above():
  if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
    return True
  else:
    return False

time_now = datetime.now()

while True:
  time.sleep(60)
  print(f"Iss current postion : {iss_latitude} {iss_longitude}")
  if is_iss_above():
    print("Lookup Now...")
    if time_now.hour >= 18 or time_now.hour <= 5:
      with smtplib.SMTP("smptp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASS)
        connection.sendmail(
          from_addr=MY_EMAIL,
          to_addrs="youremail@gmail.com",
          msg="LOOK UP!\n\nISS is passing over by"
        )
        connection.close()
  else:
    print("Checking again in 60sec")