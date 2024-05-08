import os, requests
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()
class DataManager:
#     #This class is responsible for talking to the Google Sheet.

    Sheety_End_Point = os.getenv('Sheety_End_Point')
    Sheety_UserName = os.getenv('Sheety_UserName')
    Sheety_Password = os.getenv('Sheety_Password')
    Sheety_Token = os.getenv('Sheety_Token')
    
    sheety_headers ={
    'Authorization': Sheety_Token
    }

    def get_data(self):
        resonse = requests.get(url=self.Sheety_End_Point,headers=self.sheety_headers)
        self.sheet_data = resonse.json()['prices']    
        return self.sheet_data