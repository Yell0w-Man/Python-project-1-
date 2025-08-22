
from fastapi import FastAPI, Request
import requests


app = FastAPI()

API_KEY = "65aae5b3b2d8901f3fc65c185bfb5d58"


def get_location_and_weather(ip: str):
    # --- Task 1: Get location from IP ---
    url = f"http://ip-api.com/json/{ip}"
    data = requests.get(url).json()
    city = data["city"]
    country = data["country"]



    # --- Task 2: Get weather from OpenWeatherMap ---
    weather_url = (
        f"http://api.openweathermap.org/"
        f"q={city}&appid={API_KEY}&units=metric"
    )
    weather_data = requests.get(weather_url).json()
    temperature = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]

    return city, country, temperature, description


# Task 3: return both the weather and the location details
@app.get("/report")
def report(request: Request):
    ip = request.headers.get("X-Forwarded-For", request.client.host)
    city, country, temperature, description = get_location_and_weather(ip)

    return {
        "message": f"The location is {country} ({city}), "
                   f"the temperature is {temperature}°C, "
                   f"and the weather is {description}."
    }





























# app = FastAPI()

# @app.get("location")
# def get_location(request: Request):
    
#     ip = request.headers.get("X-Forwarded-For", request.client.host)

#     #call the api
#     url = f"http://ip-api.com/json/{ip}"
#     response = requests.get(url).json()

#     #get city and country
#     city = response.get("city")
#     country = response.get("country")

#     return {
#         "ip": ip,
#         "city": city,
#         "country": country
#     }



