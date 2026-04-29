import smtplib
import requests
from datetime import datetime
import smtplib

MY_EMAIL = "[EMAIL_ADDRESS]"
MY_PASSWORD = "[PASSWORD]"

MY_LAT = "[Your Latitude]"
MY_LONG = "[Your Longitude]"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead():
    if iss_latitude < MY_LAT + 5 and iss_latitude > MY_LAT - 5 and iss_longitude < MY_LONG + 5 and iss_longitude > MY_LONG - 5:
        return True
    else:
        return False

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

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
if is_iss_overhead() and time_now.hour > sunset and time_now.hour < sunrise:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: ISS!\n\nLook up! ISS is close by."
        )
else:
    print("No ISS")



