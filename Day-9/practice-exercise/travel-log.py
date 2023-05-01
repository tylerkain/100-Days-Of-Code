travel_log = []

country = input("Type country to add: ")
num_cities = int(input("How many cities to add: "))
cities = []
i = 0
while i < num_cities:
    city = input("Enter City: ")
    cities.append(city)
    i += 1

num_visits = int(input("How Many Visits: "))


def add_new_country(country_vistied, cities_visited, visits):
    new_country = {"country": country_vistied, "cities": cities_visited, "visits": visits}
    travel_log.append(new_country)


add_new_country(country, cities, num_visits)
print(travel_log)
