from art import logo , vs
from data import data
import random as rd
import os



#function for selection of data from data file which is imported 
def data_selection():
    choice = rd.choice(data)
    return choice


def checkAnswer(userguess,account_A_followers,account_B_followers):
    if account_A_followers>account_B_followers:
        return userguess == 'a'
    if account_B_followers>account_A_followers:
        return userguess == 'b'

def format_data(account_data):
    account_name = account_data['name']
    account_desc = account_data['description']
    account_country = account_data['country']
    return f'{account_name} , a {account_desc} from {account_country}'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def game():
    should_continue = True
    score = 0
    account_A = data_selection()
    account_B = data_selection()
    while should_continue:
        account_A = account_B
        account_B = data_selection()
        print(logo)
        while account_A == account_B:
            account_B = data_selection()
        
        account_A_followers = account_A['follower_count']
        account_B_followers = account_B['follower_count']
        print(f"Compare A: {format_data(account_A)}")
        print(vs)
        print(f"Against B: {format_data(account_B)}")
        
        userguess = input("Which has more followers ? Type 'A' or 'B'= ")
        istrue = checkAnswer(userguess,account_A_followers,account_B_followers)
        clear_screen()
        if istrue:
            score+=1
            print(f"You're right! Your Current Score = {score}")
        else:
            print(logo)
            print("Buddy you're wrong")
            print(f"Your Final Score = {score}")
            should_continue = False


game()




# def game():
#     game_on = True
#     score = 0
#     while game_on:
#         print(logo)
#         choice = data_selection()
#         print("Comapare A :",choice['name'] ,",",choice['description'],"," "from ",choice['country'])
#         followers = choice['follower_count']
#         print(followers)
#         print(vs)
#         choice2 = data_selection()
#         print("Against B :",choice2['name'] ,",",choice2['description'],"," "from ",choice2['country'])
#         followers2 = choice2['follower_count']
#         print(followers2)
#         if followers > followers2:
#             answer = 'A'
#         else:
#             answer = 'B'
#         userInput = user_input()
#         if userInput == answer:
#             score+=1
#             print(f"You're right! Current score is = {score}")
#         else:
#             print(f"You're right! Current score is = {score}")
#             game_on = False

# #starting point of the python file
# if __name__ == "__main__":
#     should_continue = True
#     while should_continue:
#         game()
#         asking = input('want to play more = ').lower()
#         if asking =='n':
#             should_continue = False
    
    
