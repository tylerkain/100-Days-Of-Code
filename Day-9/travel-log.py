travel_log = []

country = input("Type country to add: ")

def add_new_country(country_vistied, cities_visited, visits):
    new_country = {"country": country_vistied, "cities": cities_visited, "visits": visits}
    travel_log.append(new_country)



add_new_country(country, 2)
print(travel_log)