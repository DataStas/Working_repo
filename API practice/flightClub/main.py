#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime as dt
from datetime import timedelta
FROM_CITY_CODE = 'LON'

d = DataManager()
# d.add_info(city="Moskow", code="MSK", price=100)
sheets = d.get_info()
# f = FlightSearch()
ans = []
f = FlightSearch()

print(f.check_flights(FROM_CITY_CODE, "BER",
                    dt.now(), dt.now()+timedelta(days=40)))
    