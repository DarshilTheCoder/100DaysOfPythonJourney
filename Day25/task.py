import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# print(data['Primary Fur Color'])
gray_count = len(data[data['Primary Fur Color']=='Gray'])
black_count = len(data[data['Primary Fur Color']=='Black'])
cinnamon_count = len(data[data['Primary Fur Color']=='Cinnamon'])
# print(gray_count)
# print(black_count)
# print(cinnamon_count)

data_dict = {
    'Fur Color':['Gray','Black','Cinnamon'],
    'Count':[gray_count,black_count,cinnamon_count]
}
new_dataFrame = pd.DataFrame(data_dict)
print(new_dataFrame)
new_dataFrame.to_csv('squirle.csv')
