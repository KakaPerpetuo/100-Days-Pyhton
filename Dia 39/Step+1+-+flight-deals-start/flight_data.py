class FlightData:
    def __init__(self, price, origin_city_code, destination_city_code, out_date, return_date):
        self.price = price
        self.origin_city_code = origin_city_code
        self.destination_city_code = destination_city_code
        self.out_date = out_date
        self.return_date = return_date

    def find_cheapest_flight(data, return_date):
        # Handle empty data if no flight data is returned
        if data is None or (not data.get("best_flights") and not data.get("other_flights")):
            print("No flights data")
            return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

        # Get data for a flight
        flights_list = data.get("best_flights", []) + data.get("other_flights", [])
        
        first_flight = flights_list[0]
        lowest_price = first_flight["price"]
        origin = first_flight["flights"][0]["departure_airport"]["id"]
        destination = first_flight["flights"][-1]["arrival_airport"]["id"]
        out_date = first_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]

        # Find the cheapest flight. Use FlighData to help you
        cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
        
        for flight in flights_list:
            try:
                price = flight["price"]
            except KeyError:
                print("---No price data---")
                continue
            
            if price < lowest_price:
                lowest_price = price
                origin = flight["flights"][0]["departure_airport"]["id"]
                destination = flight["flights"][-1]["arrival_airport"]["id"]
                out_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0]

                cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)

        return cheapest_flight
