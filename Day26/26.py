#Day26 Learning List Comprehension which is very useful in order to append the modified thing into a list , Also we can check the conditions
#Learning Dictionary Comprehension

# numbers = [1,2,3,4]
numbers=[5,6,7,8]
#List Comprehension
new_list_number = [i+1 for i in numbers]

#Normal way to append or insert into List
# for i in numbers:
#     add = i+1
#     new_list_number.append(add)
print(new_list_number)

name = "Darshil"
#Basically here letter go through each char of the name and add to new_list
new_list = [letter for letter in name]
print(new_list)

#Similarly here also i go through each number in range and each number get's multiplied by 2 and add into new_range list
new_range = [i*2 for i in range(1,5)]
print(new_range)

names = ['Darshil','Diksha','Jasmine','Jenil','Vedant','Mann']
new_names_list = [name.upper() for name in names if len(name)>5]
print(new_names_list)

#Dictionary Comprehension
import random as rd
names_dict ={student_name:rd.randint(1,100) for student_name in names}
print(names_dict)
passed_students = {student:score for (student,score) in names_dict.items() if score>60} #dict.items() method returns a object of key,value pair of dict , as tuples in a
print(passed_students)

#Looping through Dataframes in pandas using iterrows()

student_dict ={
    'student_names':['darshil','jenil','vedant','mann'],
    'score':[56,64,23,64]
}
#Normal way of iterating in dictionary
# for key in student_dict:
#     print(key)
#     print(student_dict[key])

#Easiest way of iterating over dict
# for (key,value) in student_dict.items():
#     print(key)
#     print(value)


#Looping in dataframe
import pandas as pd
student_data = pd.DataFrame(student_dict)
print(student_data)
for (index,row) in student_data.iterrows():
    # print(index)
    # print(row)
    if row.student_names == 'darshil':
        print(row.score)