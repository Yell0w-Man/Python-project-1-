from fastapi import FastAPI 

import requests

app = FastAPI()

url = "http://localhost:800/weather/?city=Lagos"

API_KEY = "d706e7e402ea937222f85b6db99fb6dc"

@app.get("/weather/")
async def get_weather(city: str = );
params = {
    "q": city;
    "appid": API_KEY;
    "units": "metric"
}
response = requests.get(url, params=params)

weather-app = response.json()

print