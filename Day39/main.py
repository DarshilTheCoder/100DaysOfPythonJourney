#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager

data = DataManager()
sheet_data = data.get_data()
for i in sheet_data:
    pass