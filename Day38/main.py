import os,requests, datetime as dt
from dotenv import load_dotenv

load_dotenv()

nutrition_api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
Nutrition_ID = os.getenv('Nutrition_ID')
Nutrition_API_KEY = os.getenv('Nutrition_API_KEY')
Sheety_End_Point = os.getenv('Sheety_End_Point')
Sheety_UserName = os.getenv('Sheety_UserName')
Sheety_Password = os.getenv('Sheety_Password')
Sheety_Token = os.getenv('Sheety_Token')


query = input('Tell me which exercise you did = ')
body = {
    'query':query
}
headers = {
    'x-app-id': Nutrition_ID ,
    'x-app-key': Nutrition_API_KEY
}
response = requests.post(url=nutrition_api_endpoint,json=body,headers=headers)
data= response.json()['exercises'][0]
duration = data['duration_min']
calories = data['nf_calories']
exercise = data['name'].title()

print(exercise)
print(duration)
print(calories)

now = dt.datetime.now()
formatted_date = now.strftime("%d/%m/%Y")
formatted_time = now.strftime('%X')


sheety_add_row_api_endpoint = Sheety_End_Point

body = {
    'workout': {
        'date':formatted_date,
        'time':formatted_time,
        'exercise': exercise,
        'duration':duration,
        'calories':calories
    }
}


sheety_headers ={
    'Authorization': Sheety_Token
}

#Basic Auth way
# sheety_add_row_response = requests.post(url=sheety_add_row_api_endpoint,json=body,auth=(
#     Sheety_UserName,
#     Sheety_Password
# ))

sheety_add_row_response = requests.post(url=sheety_add_row_api_endpoint,json=body,headers=sheety_headers)
print(sheety_add_row_response.text) 
