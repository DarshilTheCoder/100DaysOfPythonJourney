from art import logo
import random as rd


def guessing_game(attempts):

    computer_number = rd.randint(1,100)
    print(computer_number)


    def user_input():
        userInput = int(input("Make a guess = "))
        return userInput

    while attempts>0:
        userValue = user_input()
        if userValue == computer_number:
            print("Right Guess")
            break
        else:
            attempts -= 1
            print(f'You have {attempts} remaining to guess the number. ')
            if userValue > computer_number:
                print("Too high")
            else:
                print("Too Low")
            
    should_continue = True
    while should_continue:
        asking = input("Want to play more. Type 'yes' or 'no' for no more = ")
        if asking == 'no':
            print("Thanks for Playing!!")
            should_continue = False
            break
        else:
            print(logo)
            print("Welcome to the Number Guessing Game !")
            print("I'm thinking of a numnber between 1 and 100 ")
            difficulty = input("Choose the difficulty. Type 'easy' or 'hard' : ")
            if difficulty == 'easy':
                attempts = 10
            else:
                attempts = 5
            guessing_game(attempts)


if __name__ == "__main__":
    print(logo)
    print("Welcome to the Number Guessing Game !")
    print("I'm thinking of a numnber between 1 and 100 ")
    difficulty = input("Choose the difficulty. Type 'easy' or 'hard' : ")
    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5
    guessing_game(attempts)