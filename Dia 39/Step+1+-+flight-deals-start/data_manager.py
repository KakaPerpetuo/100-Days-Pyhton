from requests import request
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import requests

load_dotenv()

SHEET_PRICES_ENDPOINT = "https://api.sheety.co/da254a71ccc25659c0bb3d4e41ed8ca3/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.user = os.getenv("SHEET_USERNAME")
        self.password = os.getenv("SHEET_PASSWORD")
        self.authorization = HTTPBasicAuth(self.user, self.password)
        self.destination_data = {} 

    def get_destination_data(self):
        response = requests.get(url=SHEET_PRICES_ENDPOINT, auth=self.authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_lowest_price(self, row_id, price):
        new_data = {
            "price": {
                "lowestPrice": price,
            }
        }
        requests.put(
            url=f"{SHEET_PRICES_ENDPOINT}/{row_id}",
            json=new_data,
            auth=self.authorization
        )
