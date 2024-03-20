#Day 13 going to understand how to solve bug and find bug

############DEBUGGING#####################
# # Describe Problem
def my_function():
    for i in range(1, 20+1): #range function will no include 20th no. 
        if i == 20:
            print("You got it")
my_function()

# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) #error is list out of the index coz in list starts from 0 and here randint() consist of 1 to 6 but 6 is not there in list hence it gives this kind of error
dice_num = randint(0,5)
print(dice_imgs[dice_num])

# # Play Computer
year = int(input("What's your year of birth? "))
if year >= 1980 and year <= 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")

# # Fix the Errors
age = int(input("How old are you? "))
if age > 18:
    print(f'You can drive at age {age}.')

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
print(pages)
# word_per_page == int(input("Number of words per page: ")) # here == use for comparsion
word_per_page = int(input("Number of words per page: "))
print(word_per_page)
total_words = pages * word_per_page
print(total_words)

# #Use a Debugger 
#python tutor is best debugger inorder to solve the bug 
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])

#Take a Break (while try to tackle the )
#Ask a Friend (it will help you)
#Run Often (means run your code often , even after evey single change)
#Ask to StackOverFlow ()