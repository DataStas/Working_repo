import requests
from datetime import datetime as dt

api_key = "2c6d5e7c247486969be17893f325b971"
OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast' # 5 day 3 hour


parameters = {
    'q': "Tomsk,RU",
    'appid': api_key
}

response = requests.get(url=OWM_Endpoint,
                        params=parameters)
print(response.status_code)
response.raise_for_status()
data = response.json()



# is_night = dt.now()
weather_for_next_12 = []
umbrella_check = False
for weather in data['list'][0:4]:
    weather_for_next_12.append(weather['weather'][0]['description'])
    if weather['weather'][0]['id'] // 100 == 5:
        umbrella_check = True


if umbrella_check:
    print(weather_for_next_12)
