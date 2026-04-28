country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # Create list from formatted string

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
    },
]

def add_new_country(new_country, new_visits, new_list_cities):    # Assim que adiciona o dicionario na lista
    travel_log.append({
        "country": new_country,
        "visits": new_visits,
        "cities": new_list_cities,
    })

### Outra forma de fazer
# def add_new_country(name, times_visited, cities_visited):
#    new_country = {}
#    new_country["country"] = name
#    new_country["visits"] = times_visited
#    new_country["cities"] = cities_visited
#    travel_log.append(new_country)

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favorite city was {travel_log[2]['cities'][0]}")