weather_data = {
    "Tehran": {"temp": 28, "condition": "Sunny"},
    "Vancouver": {"temp": 18, "condition": "Cloudy"},
    "Toronto": {"temp": 20, "condition": "Rainy"},
    "Winnipeg": {"temp": 15, "condition": "Windy"}
}

while True:
    city = input("Enter city name (or 'quit' to exit): ")
    if city.lower() == "quit":
        break
    if city in weather_data:
        data = weather_data[city]
        print(f"{city}: {data['temp']}°C, {data['condition']}")
    else:
        print("City not found in mock database.")
