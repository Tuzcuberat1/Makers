import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
basic = HTTPBasicAuth('user', 'pass')

API_KEY = "d17d6c25b3ecded24f37d0dc1e81a44f"
APP_ID = "663abd2d"
SHEET_ENDPOINT = "https://api.sheety.co/39db05ab294058d2eb1e535bd24f5399/myWorkoutsStrikerEureka/workouts"

GENDER = "male"
HEIGHT_CM = "183"
WEIGHT_KG = "67"
AGE = "16"

TOKEN = "UGRfUhhwruhw89eryhefuhlj620dbs72md02gdlBF89dnN7gıyh"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

bearer_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

time = datetime.now()
date = time.strftime("%Y/%m/%d")
hour = time.strftime("%X")

response = requests.post(exercise_endpoint, json=parameters, headers=headers, auth=basic)
result = response.json()


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": hour,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs, auth=basic)
