import requests

API_KEY = "asasdasdasd"
BASE_URL = "http://api.weatherapi.com/v1"

def get_current_weather(city):
    endpoint = f"{BASE_URL}/current.json"
    params = {
        "key": API_KEY,
        "q": city
    }

    response = requests.get(endpoint, params=params)

    data = response.json()
    # print(data)

    location = data["location"]["name"]
    country = data["location"]["country"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    humidity = data["current"]["humidity"]
    feelslike_c = data["current"]["feelslike_c"]
    
    print(f"Weather in {location}, {country}:")
    print(f"Temperature: {temp_c}°C (Feels like: {feelslike_c}°C)")
    print(f"Condition: {condition}")
    print(f"Humidity: {humidity}%")

get_current_weather("Dhaka")
get_current_weather("Rajshahi")
get_current_weather("Chittagong")