import requests,json
MY_LAT = 22.307159
MY_LNG = 73.181221
# response = requests.get(url='http://api.open-notify.org/iss-now.json')

# response.raise_for_status() #it will raise an HTTP Error on unsuccessfull status
# data = response.json()["iss_position"]
# iss_longitude = data['longitude']
# iss_latitude = data['latitude']
# data2 = (iss_longitude,iss_latitude)
# print(data)
# print(data2)
parameters = {
    'lat':MY_LAT,
    'lng':MY_LNG,
    'formatted':0
}
response2 = requests.get(url='https://api.sunrise-sunset.org/json',params=parameters,)
response2.raise_for_status()
data3 = response2.json()['results']
sunrise = data3['sunrise']
print(sunrise.split('T')[1].split(':')[0])
sunset = data3['sunset']
result= (sunrise,sunset)
print(result)