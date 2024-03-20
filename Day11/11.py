#first capstone project is Black Jack Game 
#Requirement list = rd.choice() , 
# list[] will store 1 to 10 no. , 
# append method to append user value in list 
# score calc 
# for loop will use , 
# while loop will also use to ask whether to continue the game or not , 

import random as rd 
card_list = [1,2,3,4,5,6,7,8,9,10,10,10,10]
user_card_list = []
computer_card_list = []
want_to_play = input("Want to play BlackJack Card game, type 'y' for play and 'n' for not = ")


def user_score_cal(user_card_list):
    user_score = 0
    for i in user_card_list:
        user_score+=i
    return user_score

def computer_score_cal(computer_card_list):
    computer_score = 0
    for i in computer_card_list:
        computer_score+=i
    return computer_score

def user_card_selector(card_list):
    card = rd.choice(card_list)
    user_card_list.append(card)
    print(f'user score is = {user_score_cal(user_card_list)}')
    return user_card_list

def computer_card_selector(card_list):
    computer_score = 0
    card = rd.choice(card_list)
    computer_card_list.append(card)
    print(f'computer score is = {computer_score_cal(computer_card_list)}')
    return computer_card_list


if __name__ == '__main__':
    if want_to_play == 'y':
        
        user_cards = user_card_selector(card_list)
        user_cards = user_card_selector(card_list)
        computer_cards = computer_card_selector(card_list)
        computer_cards = computer_card_selector(card_list)
        print(user_cards)
        print(computer_cards)
