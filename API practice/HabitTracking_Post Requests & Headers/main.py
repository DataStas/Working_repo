
import requests
import json
from datetime import datetime as dt

pixela_endpoint = 'https://pixe.la/v1/users'

# user_params = {
#     'token': 'token',
#     'username': 'name',
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes',
#     'response': ""
# }

# with open('settings.json', 'w') as file:
#     json.dump(user_params, file)
# response = requests.post(url=pixela_endpoint,
#                          json=user_params)
# print(response.text)


with open('settings.json', 'r') as file:
    user_params = json.load(file)

# graph_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs"
# graph_params = {
#     'id': 'graphcoding1',
#     'name': 'coding graph',
#     'unit': 'min',
#     'type': 'int',
#     'color': 'shibafu',
# }

headers = {
    "X-USER-TOKEN": user_params['token']
}
# response = requests.post(url=graph_endpoint,
#               json=graph_params,
#               headers=headers)
# print(response.text)

# record_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{user_params['id']}"

# record_params = {
#     'date': dt.now().strftime('%Y%m%d'),
#     'quantity': '120'
# }

# response = requests.post(url=record_endpoint, 
#                          json=record_params,
#                          headers=headers)
# print(responce.text)


# update_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{user_params['id']}/20230510"

# update_params = {
#     'quantity': '180'
# }
# response = requests.put(url=update_endpoint, 
#                          json=update_params,
#                          headers=headers)
# print(responce.text)

# put POST - это INSERT, а PUT - UPDATE or INSERT PUT обязан обновлять запись!

delete_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{user_params['id']}/20230510"

response = requests.delete(url=delete_endpoint,
                        headers=headers)
print(response.text)