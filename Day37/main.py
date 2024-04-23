import requests
import datetime as dt

USERNAME = 'darshil2002'
TOKEN = 'slk432df2p4u3h2409s'
ID = 'darshil02'
pixela_endpoint = "https://pixe.la/v1/users"

user_param2 = {
    'token':TOKEN,
    'username':USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
}

# response = requests.post(url=pixela_endpoint,json=user_param2)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id':ID,
    'name':'Coding',
    'unit':'commit',
    'type':'int',
    'color':'shibafu',
    'timezone':'Asia/Calcutta'
}

graph_headers ={
    'X-USER-TOKEN':TOKEN
}

# graph_response= requests.post(url=graph_endpoint,json=graph_config,headers=graph_headers)
# print(graph_response.text)

create_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
def get_date():
    date = dt.datetime.now().date()
    date_list = date.strftime("%Y-%m-%d").split("-")
    formatted_date = "".join(date_list)
    return str(formatted_date)

create_pixel_config = {
    'date':get_date(),
    'quantity':'5',
}

create_pixel_response = requests.post(url=create_pixel_endpoint,json=create_pixel_config,headers=graph_headers)
print(create_pixel_response.text)

