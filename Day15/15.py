#Day15 of learning 100days of Python 
#Project Coffee Machine 
#Program Requirements 
'''
1. Print Report 
2. Check resources sufficient 
3. Process Coins
4. Check transaction successful
5. Make Coffee
'''
from data import MENU,resources




# def show_report():
#     # Add code here to display the report
#     print(f'water : {resources["water"]}ml')
#     print(f'milk : {resources["milk"]}ml')
#     print(f'coffee : {resources["coffee"]}g')

# def check_sufficient_resource(selected_coffee,MENU,resources):
#     count = 0
#     if resources["water"]>=MENU[selected_coffee]["ingredients"]["water"]:
#             count+=1
#     if resources["milk"]>=MENU[selected_coffee]["ingredients"]["milk"]:
#             count+=1
#     if resources["coffee"]>=MENU[selected_coffee]["ingredients"]["coffee"]:
#             count+=1
#     if count ==3:
#         return True
#     else:
#         return False
    

# def calculation(selected_coffee):
#     twoHundredNote = int(input('how many 200 notes? = '))
#     oneHundredNote = int(input('how many 100 notes? = '))
#     fiftyRupeeNote = int(input('how many 50 rupee note? = '))
#     twentyRupeeNote = int(input('how many 20 rupee notes? = '))
#     given_amount = twoHundredNote + oneHundredNote + fiftyRupeeNote + twentyRupeeNote
#     cost_of_selected_coffee = MENU[selected_coffee]["cost"]

#     if given_amount > cost_of_selected_coffee:
#         print(f"Here's your Rs{given_amount - cost_of_selected_coffee} in change")
#         print(f"Here's your {selected_coffee}")        

#     elif given_amount < cost_of_selected_coffee:
#         print('Please enter proper amount')
#         calculation()
#     else:
#         print("Your given amount is perfect")

# def making_coffee():
#     user_choice = input("Would you like to take? (espresso/latte/cappuccino): ")
#     if user_choice == 'report':
#         show_report()
#     else:
#         if check_sufficient_resource(user_choice,MENU,resources):
#             calculation(user_choice)
#         else:
#             print("Not enough resources")

# making_coffee()