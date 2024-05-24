import datetime

import requests
from requests.auth import HTTPBasicAuth

date = datetime.date.today().strftime("%d/%m/%Y")
time = datetime.date.today().strftime("%X")
sheet_endpoint = "https://api.sheety.co/b86cf954ccd28198f30fa922eef4ee6a/myWorkouts/workouts"
APP_ID = "9372ca8a"
API_KEY = "9d8adaead59beaeb558d77f6e928675a"
age = "21"
gender = "male"
weight = "65"
height = "170"

exercise_text = input("Tell me which exercises you did: ")
endpoint_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
params = {
    'query': exercise_text,
    "gender": gender,
    "weight_kg": weight,
    "height_cm": height,
    "age": age
}

response = requests.post(url=endpoint_url, json=params, headers=header)
result = response.json()

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    bearer_headers = {
        "Authorization": "Basic R2hlb3JnaGk6MDY5NjE0MzYz"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers,
        auth=HTTPBasicAuth(username="Gheorghi", password="069614363")
    )
    print(sheet_response.text)
