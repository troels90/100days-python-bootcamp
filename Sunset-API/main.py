import requests
from datetime import datetime

parameters = {
    "lat": 55.676098,
    "lng": 12.568337,
    "formatted":0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

time_now = datetime.now()
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
print(sunset)
print(sunrise)
print(time_now.hour)