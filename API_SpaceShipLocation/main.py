import requests
from datetime import datetime as dt
# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# # if response.status_code != 200:
# #     raise Exception('Bad response from ISS API')
# # if response.status_code == 404:
# #     raise Exception('That resource does not exist.')
# # if response.status_code == 401:
# #     raise Exception('You.')
# response.raise_for_status() # if we dont get 200 (pass) we will see an exception
# data = response.json()
# # longitude = response.json()['iss_position']['longitude']
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']

# iss_position = (longitude, latitude)

# print(iss_position)

MY_LAT = 56.4911
MY_LONG = 84.9949
parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}
response = requests.get('http://api.sunrise-sunset.org/json', params=parameters)
# http://api.sunrise-sunset.org/json?lat=56.4911&lng=84.9949
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(':')[0]
sunset = data['results']['sunset'].split("T")[1].split(':')[0]
time_now = dt.now()
print(sunrise,
      sunset,
      time_now.hour)