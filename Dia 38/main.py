import requests
import datetime as dt
import os

APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")

USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")

app_url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheet_endpoint = "https://api.sheety.co/da254a71ccc25659c0bb3d4e41ed8ca3/workoutTracking/workouts"

exercise_text = input("Tell me which exercise you did: ")

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

app_data = {
    "query": exercise_text,
    "weight_kg": 60,                  
    "height_cm": 168,                 
    "age": 25,                        
    "gender": "female"                  
}

response = requests.post(url=app_url, headers=headers, json=app_data)
result = response.json()

today_date = dt.datetime.now().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%H:%M:%S")

for exercise in result["exercises"]:
    sheety_post_data = {
        "workout": {
            "date": today_date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(
        sheet_endpoint,
        json=sheety_post_data,
        auth=(
            USER,
            PASSWORD
        )
    )

    print(sheety_response.text)