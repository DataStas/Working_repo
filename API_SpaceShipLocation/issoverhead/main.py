import requests
from datetime import datetime
import smtplib
from datetime import time

MY_LAT = 56.4911  # Your latitude
MY_LONG = 84.9949  # Your longitude



# Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if abs(iss_latitude-MY_LAT) < 5 and abs(iss_longitude-MY_LONG) < 5:
        return True
    else:
        False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json",
                            params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 7 - 24
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 7
    time_now = datetime.now().hour
    if sunrise >= time_now or sunset <= time_now:
        return True

            
def send_email():
    with open("../../email_send/SmtpTests/emailSender/email_info.txt", 'r') as file:
        lines = file.read().split()
        my_email = lines[0]
        my_password = lines[1]
    with smtplib.SMTP('smtp.gmail.com') as connection: # host name
        # Transpot Layer Security
        connection.starttls()  # make connection crepted and secure
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="forworkpenguinlolo@gmail.com",
                            msg='Subject:Hello\n\n THERE IS A SPACE SHIP CLOSE TO YOU!!!'
                            )
            
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.


# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        send_email()


