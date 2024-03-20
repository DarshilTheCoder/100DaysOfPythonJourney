
def greet(name):
    print(f'hello how do you do {name}')
    print(f'we wll meet oneday {name}')

name = input("what's your name = ")
greet(name)

def sum(a,b):
    x = a 
    y = b
    print(f'value of x is {x} and value of y is {y}')
    c =x+y 
    return c

print(sum(b=3,a=5))
print(sum(4,1))

#Day8 project Cieser Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
game_on = True
while game_on:
    def ceaser_cipher2(start_text,shift_amount,direction):
        end_text=""
        if direction == "2":
            shift_amount*= -1
        for letter in start_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                new_char = alphabet[new_position]
                end_text+=new_char
            else:
                end_text+=letter
        print(f'your end value is {end_text}')

    direction = input("What do you want to do 1 for 'encryption' or 2 for 'decryption'")
    string_value = input("Enter the input value = ").lower()
    shift_amount = int(input("Enter the shift_amount = "))
    shift_amount = shift_amount % 26
    ceaser_cipher2(string_value,shift_amount,direction)
    asking = input("would you like to game on = ")
    if asking == 'no':
        game_on = False
        print("Thank you for playing")

# def encryption(text,shift_amount):
    

# def decryption(text,shift_amount):
    

# def ceaser_cipher(text,shift_amount,direction):
#     if direction =="1":
#         ciser_cipher = ""
#         for letter in text:
#             position = alphabet.index(letter)
#             new_position = position + shift_amount
#             new_char = alphabet[new_position] 
#             ciser_cipher+=new_char
#         print(f'encrypted code is = {ciser_cipher}')
#     else:
#         decipher = ""
#         for letter in text:
#             position = alphabet.index(letter)
#             new_position = position - shift_amount
#             new_char = alphabet[new_position] 
#             decipher+=new_char
#         print(f'decrypted code is = {decipher}')