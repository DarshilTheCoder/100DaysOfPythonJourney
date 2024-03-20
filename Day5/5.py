#Day5 Loops
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)

#for loop using range
total= 0
for number in range(1,101):
    total+=number
print(total)

for i in range(2,11,2):
    print(i)

#Day5 Project Password Generator
import random as rd
import string  
letters = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation
print("Welcome to Password Generator")
letter_count = int(input("How many letters would you like in your password?\n"))
number_count = int(input("How many numbers would you like in your password?\n"))
punctuation_count = int(input("How many punctuation would you like in your password?\n"))
password = ""
for i in range(0,letter_count):
    password+=rd.choice(letters)
for i in range(0,number_count):
    password+=rd.choice(numbers)
for i in range(0,punctuation_count):
    password+=rd.choice(punctuation)
print(password)

password =""
#Another way to do this
for i in range(0,letter_count):
    password+=rd.choice(letters)
for i in range(0,number_count):
    password+=rd.choice(numbers)
for i in range(0,punctuation_count):
    password+=rd.choice(punctuation)
password_list = list(password)
print(password_list)
rd.shuffle(password_list)
print(password_list)
password = ''.join(password_list) # it is used to join password list
print(password)