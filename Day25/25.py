# with open('weather_data.csv',mode='r') as csvFileReader:
#     csvFileContent = csvFileReader.readlines()
#     print(csvFileContent)

# import csv

# with open('weather_data.csv',mode='r') as csvDataFile:
#     data = csv.reader(csvDataFile)
#     temperature = []
#     for row in data:
#         print(row[1])
#         if row[1] == 'temp':
#             continue
#         else:
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas as pd
data = pd.read_csv('weather_data.csv')
print(type(data)) #it will show that it is object
print(data['temp'])

# data_dict = data.to_dict()
# print(data_dict)

temp_list = data['temp'].tolist()
# print(temp_list.__sizeof__())
# temp_sum = 0
# for temp in temp_list:
#     temp_sum = temp_sum + temp
# print("Avg temp = ",sum(temp_list)/len(temp_list))
# print(data['temp'].mean())
# print(data['temp'].max())

#Get Data from Column
print(data['condition']) #here condition is treated as a object
print(data.condition) #here condition is treated as a attribute 

#Get Data from a perticular Row 
print(data[data['day']== 'Monday'])

#challenge
# max_temperature = data['temp'].max()
# print(data[data['temp']==max_temperature])

#challenge
# row = data[data['day']=='Monday']
# monday_temp = (row['temp'] *(9/5))+32
# print(monday_temp)

#Creating DataFrame from sctrach
data_dict ={
    'students':['darshil','jenil','vedant'],
    'marks':[67,76,88]
}

data_dataFrame = pd.DataFrame(data_dict)
print(data_dataFrame)
data_dataFrame.to_csv('new_datafile.csv')
