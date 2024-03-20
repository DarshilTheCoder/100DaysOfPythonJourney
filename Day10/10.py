#going to learn Functions with Outputs 

def calc(a,b):
    sum = a + b

    return sum

def format_name(f_name,l_name):
    """ Take a first and last name and format it to return the title case version of the name.""" #docstring 
    final_name = f_name.upper() + " "+ l_name.upper()
    return final_name
a = int(input("enter the value of a = "))
b = int(input("enter the value of b = "))
first_name = input("enter the first name = ")
last_name = input("enter the last name = ")
calci = calc(a,b)
print(calci)
name = format_name(first_name,last_name)
print(name)


#Day 10 Project: Calculator

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2


operations = {
    '+': add, 
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    n1 = float(input('Enter the number 1 = '))

    for key in operations:
        print(key)

    should_continue = True
    while should_continue:
        operations_symbols = input('please choose any one of the operation = ')
        n2 = float(input('Enter the number 2 = '))
        calc_function = operations[operations_symbols] #understand that how we can dynamically add the name of the function 
        answer = calc_function(n1,n2)
        print(f'{n1} {operations_symbols} {n2} =  {answer}')
        if input(f"Type 'y' to continue with {answer} or Type 'n' to start a new calculation ") =='y':
            n1 = answer
        else:
            should_continue = False
            calculator()
calculator()
# calc_on = True
# while calc_on:
#     prev_answer = first_answer
#     n3 = int(input('enter another number = '))
#     operations_symbols = input('please choose any one of the operation from above = ')
#     calc_function = operations[operations_symbols]
#     second_answer = calc_function(prev_answer,n3)
#     print(f'{first_answer} {operations_symbols} {n3} =  {second_answer}')
#     prev_answer = second_answer
#     asking = input('want to continue the calc ?? type \'yes\' or \'no\' ')
#     if asking == 'no':
#         calc_on = False
