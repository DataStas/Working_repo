import requests
import json
from flight_search import FlightSearch

class DataManager(FlightSearch):  
    def __init__(self):
        self.destination_data = {}
 
    def get_info(self) -> dict:
        self.check_destination_codes()
        with open('private_sheets.json', 'r') as file:
            hidden_info = json.load(file)
        header = {"Authorization": hidden_info['Authorization']}
        sheet_endpoint = hidden_info['API']
        sheet_response = requests.get(url=sheet_endpoint,
                                    headers=header)
        sheet_response.raise_for_status()
        self.destination_data = sheet_response.json()['my']
        return self.destination_data

    def add_info(self, city: str, code: str, price: int):
        with open('private_sheets.json', 'r') as file:
            hidden_info = json.load(file)
        header = {"Authorization": hidden_info['Authorization']}
        sheet_endpoint = hidden_info['API']
        info = {
            hidden_info['SheetName']: {
                "city": city,
                "iataCode": code,
                "lowestPrice": str(price)
            }
        }
        add_response = requests.post(url=sheet_endpoint,
                                     json=info,
                                     headers=header)
        add_response.raise_for_status()
        print(f"Your status {add_response.status_code}")

    def check_destination_codes(self):
        with open('private_sheets.json', 'r') as file:
            hidden_info = json.load(file)
        header = {"Authorization": hidden_info['Authorization']}
        sheet_endpoint = hidden_info['API']
        for city in self.destination_data:
            if city["iataCode"] == '':
                f = FlightSearch()
                new_data = {
                    hidden_info['SheetName']: {
                        "city": city["city"],
                        "iataCode": f.get_destination_code(city["city"]),
                        "lowestPrice": city['lowestPrice']
                    }
                }
                response = requests.put(
                    url=f"{sheet_endpoint}/{city['id']}",
                    json=new_data,
                    headers=header
                )
                print(response.text)