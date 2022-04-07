import requests
from datetime import datetime
import os
APP_ID = os.environ.get("API_ID")
API_KEY = os.environ.get("API_KEY")
Authorization_Token = os.environ.get("TOKEN")

USER_ID = os.environ.get("USER_NAME")
USER_PASSWORD = os.environ.get("USER_PASSWORD")

GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 180
AGE = 23

today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

headers_sheety = {
    "Authorization": Authorization_Token
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content_Type": "application/json"
}
nutritionix_endpoint_exercise = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint= os.environ.get("SHEET_ENDPOINT")


exercise_text = input("Tell me which exercises you did: ")

user_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,

}

response_nutritionix = requests.post(url=nutritionix_endpoint_exercise, json=user_params, headers=headers)
result = response_nutritionix.json()["exercises"]
len_of_exercises_list = len(result)

for exercise in result:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=headers_sheety)

# response_sheety = requests.get(url=Sheety_Endpoint, headers=headers_sheety)
# response_sheety.raise_for_status()
# print(response_sheety.text)
