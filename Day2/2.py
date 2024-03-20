#Today we are going to built a calculator in python 

#DataTypes in python 
print("Hello"[0]) #string
print(123+2) #integer
print(123.34)#float 
# True and False  this is boolean 

#Something interesting to know that 
mystery = 456_325.34  # such thing is used in python inorder to increase the readability of the code or value 
print(mystery)

print(type(int("123")))
print(type("123"))

num_char = str(len(input("What is your Name =")))

print("your name has "+num_char+" characters") #only strings can concanate 

#f-string it will be usefull so much that with this you don't have to convert everything into string while printing

score = 0
height= 1.3
isWinning = True 
print(f"your score is {score} and your height is {height} hence you are {isWinning}")

#Project2 of Day2 Tip Calculator
total_bill = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15 "))
total_person = int(input("How many people to split the bill - "))
final_value_of_bill = total_bill*(tip_percentage/100)+total_bill
split_value = round(final_value_of_bill/total_person,2)
print(f"Each person should pay : ${split_value}")
