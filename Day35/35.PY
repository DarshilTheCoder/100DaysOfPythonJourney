import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv() #used to load the env files
account_sid = os.getenv('sid')
auth_token = os.getenv('token')
client = Client(account_sid, auth_token)

MY_LAT =50.850346 # Your latitude brussel
MY_LONG = 4.351721# Your longitude brussel
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    'appid':os.getenv('appid'),
    'cnt':4
}
response = requests.get('https://api.openweathermap.org/data/2.5/forecast',params=parameters)
response.raise_for_status()
data = response.json()
weather_list = data['list']
# print(weather_list)
weather_ids = [ i['weather'][0]['id'] for i in weather_list]

#whenever you want to do list or dict comprehension try to write it first in a simple way then do it 
# weather_id = weather_dict['weather'][0]
# print(weather_list)
# for i in weather_list:
#     weather_id = i['weather'][0]['id']
#     weather_ids.append(weather_id)
print(weather_ids)
is_Rain = False
for i in weather_ids:
    if i<700:
        is_Rain = True

if is_Rain:
    message = client.messages.create(
        from_='+15074195966',
        body='Today Rain will going to take place please bring your Umbrella ☔',
        to='+919316551262')
else:
    print('no rain will going to happen')