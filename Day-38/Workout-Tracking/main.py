import requests
from datetime import datetime
import os

now = datetime.now()

sheet_endpoint = os.environ.get("sheetEndpoint")
NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutrinoxToken = os.environ.get("nutrinoxToken")

headers_nutri = {
    "x-app-id": os.environ.get("xappid"),
    "x-app-key": os.environ.get("xappkey")
}

activity = input("Enter exercise details: ")

parameter_nutri = {
    "query":activity
}

response_nutri = requests.post(url=NUTRI_ENDPOINT, json=parameter_nutri, headers=headers_nutri)
print(response_nutri.text)
result = response_nutri.json()

# print(now.strftime(f"%Y/%m/%d"), now.strftime(f"%H:%M:%S"), data["exercises"][0]["name"], data["exercises"][0]["duration_min"], data["exercises"][0]["nf_calories"])

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
print(sheet_response.text)