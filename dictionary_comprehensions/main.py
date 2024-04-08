cities_in_F = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
cities_in_C = {key: round((value - 32) * 5 / 9) for (key, value) in cities_in_F.items()}

print(cities_in_C)

weather = {"NY": "snowing", "Boston": "sunny", "LA": "sunny", "Chicago": "cloudy"}
sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}

print(sunny_weather)

desc_cities = {
    key: ("warm" if value >= 40 else "cold") for (key, value) in cities_in_C.items()
}

print(desc_cities)


def check_temp(value):
    if value >= 70:
        return "hot"
    else:
        return "normal"


desc_cities_fn = {key: check_temp(value) for (key, value) in cities_in_F.items()}

print(desc_cities_fn)
