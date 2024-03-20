#Day4 learning is Radomization and list
# Randomization is a process of generating random numbers or choosing random elements from a set of elements.
# Randomization is used in machine learning, statistics, and other fields.

import random as rd
import mymodule as mm 
random_int = rd.randint(0,2)
print(random_int)
print(mm.pi)

random_float = rd.random()*5
print(random_float)

#Learning List
# List is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item.

states_of_india = ["Guajrat","GOa","Kerala","Tamil Nadu","Maharashtra"]
print(states_of_india)
lenght = len(states_of_india)
print(lenght)
random_state =rd.randint(0,lenght-1)
print(random_state)
print(states_of_india[random_state])

#Day4 Project Rock Paper Scissors
while(True):
    print("Welcome to Rock Paper Scissors")
    user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    computer_input = rd.randint(0,2)
    print(f"Computer chose {computer_input}")
    if user_input ==0:
        if computer_input ==0:
            print("It's a Draw")
        elif computer_input ==1:
            print("You Lose")
        else:
            print("You Win")
    elif user_input ==1:
        if computer_input ==1:
            print("It's a Draw")
        elif computer_input ==0:
            print("You Win")
        else:
            print("You Lose")
    else:
        if computer_input ==2:
            print("It's a Draw")
        elif computer_input ==1:
            print("You Win")
        else:
            print("You Lose")