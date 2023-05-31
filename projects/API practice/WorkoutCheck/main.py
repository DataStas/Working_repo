
import requests
import json
from datetime import datetime as dt


def make_exercise(s: str) -> dict:
    exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

    with open('settings.json', 'r') as file:
        header = json.load(file)

    exercise_text = s
    exercise_params = {
        "query": exercise_text,
        "gender": "male",
        "weight_kg": 90,
        "height_cm": 185,
        "age": 24
    }

    response = requests.post(url=exercise_endpoint,
                            json=exercise_params,
                            headers=header)
    response.raise_for_status()

    return response.json()


def write_to_sheet(result: dict):
    with open('private.json', 'r') as file:
        hidden_info = json.load(file)

    header = {
        "Authorization": hidden_info['Authorization']
        }
    sheet_endpoint = hidden_info['API']

    # response = requests.get(url=google_sheet_endpoint,
    #                         headers=header)
    # response.raise_for_status()
    # print(response.text)
    today_date = dt.now().strftime("%d/%m/%Y")
    now_time = dt.now().strftime("%X")

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

    sheet_response = requests.post(sheet_endpoint,
                                json=sheet_inputs,
                                headers=header)
    # print(sheet_response.text)


res = make_exercise(input("Tell me which exercises you did: "))
print(res)
write_to_sheet(res)