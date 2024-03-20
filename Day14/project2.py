#logo of higher-lower game 
from art import logo,vs
from data import data
import random as rd
import os

def data_selection():
    return rd.choice(data)

def format_data(values):
    return f"{values['name']},a {values['description']},from {values['country']}"

def checkAnswer(user_input,acount_A_followers,acount_B_followers):
    if acount_A_followers>acount_B_followers:
        return user_input == 'A'
    else:
        return user_input == 'B'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def game():
    print(logo)
    score_counter = 0
    account_A = data_selection()
    account_B = data_selection()
    should_continue = True
    #loop will continue untill the condition gets false 
    while should_continue:
        account_A = account_B
        account_B = data_selection()

        while account_A == account_B:
            account_B = data_selection()
        
        # print(f"Compare A = {account_A['name']}, a {account_A['description']}, from {account_A['country']}")
        print(f"Compare A = {format_data(account_A)}")
        print(vs)
        # print(f"Against B = {account_B['name']}, a {account_B['description']}, from {account_B['country']}")
        print(f"Against B = {format_data(account_B)}")
        user_choice = input("Who has more followers? Type 'A' or 'B' = ").upper()
        isRight = checkAnswer(user_choice,account_A['follower_count'],account_B['follower_count'])
        # print(isRight)
        clear_screen()
        if isRight:
            score_counter+=1
            print(f"You're right! Your Current Score = {score_counter}")
        else:
            print(logo)
            print("Buddy you're wrong")
            print(f"Your Final Score = {score_counter}")
            should_continue = False


game()