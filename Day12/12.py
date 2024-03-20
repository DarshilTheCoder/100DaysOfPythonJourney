#Day12 learning function scope 

player_health = 10 #global scope 

def drink_potion():
    potion_strength = 2 # local scope 
    print(potion_strength)

drink_potion()

game_level = 3 
enemies = ['skeleton','zombie','dayan']

if game_level <5:
    new_enemie = enemies[0]

print(new_enemie) # this shows that there is no concept of block scope just like java,c++ and all

def game():
    if game_level <5:
        new_enemie2 = enemies[2]

    print(new_enemie2) # here error is coming coz now new_enemie2 is under local scope 
game()

#Modifying global variable in local scope
enemies = 1
def increase_enemie():
    #inorder to change global variable under local scope use "globle" keyword
    # global enemies
    # enemies+=1

    print(f'the number of enemies = {enemies}') 
    #but doing this thing will cost you big coz global variable is defined anywhere and you changed it then create a bug while using another time anywhere 
    return enemies +1 # this is best approach



enemies = increase_enemie() # here it will throw an error that "local variable 'enemies' referenced before assignment"
print(f'increased enemies = {enemies}')

#Global Constants

PI = '3.14'
URL = "www.google.com"

def name():
    PI = '3.5654'
    #as soon as you written in captial word it notifies that not to modify it 
name()