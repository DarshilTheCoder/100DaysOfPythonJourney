import requests
from datetime import datetime
import smtplib
import time
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

MY_LAT = 22.307159 # Your latitude
MY_LONG = 73.181221# Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    current_lat_value = MY_LAT-iss_latitude
    current_long_value = MY_LONG-iss_longitude


    if -5<=current_lat_value<=5 and -5<=current_long_value<=5:
        return True

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    'timezone':	'IST'
}

def check_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise+5)
    print(sunset+5)
    time_now = datetime.now()
    hours = time_now.hour
    if sunset<hours or hours<sunrise:
        return True
    
    
my_email = "darshil.coder350@gmail.com"
my_password = ""

while True:
    time.sleep(60)
    if is_iss_overhead() and check_night():
        with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
                print('connection donoe')
                connection.starttls()
                connection.login(user=my_email,password=my_password)
                connection.sendmail(from_addr='darshil.coder350@gmail.com',to_addrs='darshil.20becev124@gmail.com',msg='Subject: LOOK UP\n\n ISS going from your timezone look up look up look up !!!!')
            
#This is my way of solving
# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()
# sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
# sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
# print(sunrise+5)
# print(sunset+5)
# time_now = datetime.now()
# hours = time_now.hour
# def check_currently_dark(hour):
#     if sunset<hour or hour<sunrise:
#         return True
#     else:
#         return False
# #If the ISS is close to my current position

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()

# iss_latitude = float(data["iss_position"]["latitude"])
# iss_longitude = float(data["iss_position"]["longitude"])
# current_lat_value = MY_LAT-iss_latitude
# current_long_value = MY_LONG-iss_longitude

# if -5<=current_lat_value<=5 and -5<=current_long_value<=5:
#     # and it is currently dark
#     print('ISS is closed to your location')
#     if check_currently_dark(hours):
#         print('Night Time Right Now')
#         # Then send me an email to tell me to look up.
#         with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
#             print('connection donoe')
#             connection.starttls()
#             connection.login(user=my_email,password=my_password)
#             connection.sendmail(from_addr='darshil.coder350@gmail.com',to_addrs='darshil.20becev124@gmail.com',msg='Subject: LOOK UP\n\n ISS going from your timezone look up look up look up !!!!')
#         # server_host = "smtp.gmail.com"
#         # server_port = 587

#         # #Setup Gmail credentials
#         # my_email = "darshil.coder350@gmail.com"
#         # my_password = "werc vutc xdxz wrkv"

#         # #Sender and receiver email
#         # sender = "darshil.coder350@gmail.com"
#         # receiver ="darshil.20becev124@gmail.com"

#         # #Setup Subject and to,from
#         # msg = MIMEMultipart()
#         # msg['From'] = sender
#         # msg['To'] = receiver
#         # msg['Subject'] = "LOOK UP!!"
            
#         #     #setup body 
#         # body = "ISS going from your timezone look up look up look up !!!!"
#         # msg.attach(MIMEText(body,'plain'))
            
#         # with smtplib.SMTP(server_host,server_port) as server_connection:
#         #         print('connection done')
#         #         server_connection.starttls()
#         #         server_connection.login(user=my_email,password=my_password)
#         #         text = msg.as_string()
#         #         server_connection.sendmail(from_addr=sender,to_addrs=receiver,msg=text)
#     else:
#         print('Day time Right Now')
# else:
#     print('ISS is not closed to you')
# # BONUS: run the code every 60 seconds.



