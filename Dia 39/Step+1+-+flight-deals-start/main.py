import requests_cache
from data_manager import DataManager
from pprint import pprint
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# Conserve requests anda preserve your free plan
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

# Set the dates
tomorrow = datetime.now() + timedelta(days=1)
six_months_from_now = datetime.now() + timedelta(days=180)

# Talk to Sheety
data_manager = DataManager()
data_sheet = data_manager.get_destination_data()
#pprint(data_sheet)

flight_search = FlightSearch()
notification_manager = NotificationManager()

# Search all destinations
ORIGIN_CITY = "LHR"

for destination in data_sheet:
    pprint(f"Getting flights for {destination['city']}...")
    data_for_flights = flight_search.check_flights(
        ORIGIN_CITY, 
        destination["iataCode"], 
        from_time=tomorrow.strftime("%Y-%m-%d"), 
        to_time=six_months_from_now.strftime("%Y-%m-%d"))

    #pprint(data_for_flights)

    cheapest_flight = FlightData.find_cheapest_flight(
        data_for_flights,
        six_months_from_now.strftime("%Y-%m-%d")
    )
    pprint(f"{destination['city']}: GBD {cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price <= destination["lowestPrice"]:
        pprint(f"Low Price Flight Deal Found to {destination['city']}!")
        data_manager.update_lowest_price(destination["id"], cheapest_flight.price)
        notification_manager.send_sms(
            message_body=f"Low price alert! Only GBD {cheapest_flight.price} to fly from {cheapest_flight.origin_city_code} to {cheapest_flight.destination_city_code} from {cheapest_flight.out_date} to {cheapest_flight.return_date}"
        )


#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.