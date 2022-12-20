import time

import requests
import smtplib as smtp
from datetime import datetime

MY_LAT = 55.676098 # Your latitude
MY_LONG = 12.568337 # Your longitude


def iss_nearby():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    if iss_latitude-5 < MY_LAT < iss_latitude+5 and iss_longitude-5 < MY_LONG < iss_longitude+5:
        return True


def is_it_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now <= sunrise or time_now >= sunset:
        return True




while True:
    time.sleep(60)
    print("Checking")
    if iss_nearby() and is_it_dark():
        my_email = "troelstesting@hotmail.com"
        password = "abctest123"
        to_email = "troelsp@gmail.com"
        title = "ISS Lookup!"
        message = "The international space station is close, lookup!"

        with smtp.SMTP("smtp.office365.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f"Subject:{title}\n\n{message}"
            )



