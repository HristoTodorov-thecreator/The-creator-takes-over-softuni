
def forecast(*args):
    weather_order = {"Sunny": 0, "Cloudy": 1, "Rainy": 2}
    locations = []

    for arg in args:
        location ,weather = arg
        locations.append((weather_order[weather], weather, location))

    locations.sort(key=lambda x: (x[0], x[2]))


    output = []
    for loc in locations:
        output.append(f"{loc[2]} - {loc[1]}")

    return '\n'.join(output)




print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))