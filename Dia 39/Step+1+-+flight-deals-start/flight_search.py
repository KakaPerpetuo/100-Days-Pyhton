import os
from dotenv import load_dotenv
import requests

load_dotenv()

GOOGLE_FLIGHTS_API = "https://serpapi.com/search"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = os.getenv("SERPAPI_API_KEY")
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query_params = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time,
            "return_date": to_time,
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self.api_key,
        }

        response = requests.get(url=GOOGLE_FLIGHTS_API, params=query_params)
        data = response.json()
        return data
        