#Day7 of learning going to create a hangman project today is 
import random as rd

word_list =['darshil','diksha','jenil','jasmine']
# word_list = ["darshil","diksha","jenil","jasmine"]

choosen_word = rd.choice(word_list)
print(choosen_word)
length_of_choosen_word = len(choosen_word)
display = []
for _ in range(length_of_choosen_word):
    display +="_"
print(display) 

lives = 3
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter ").lower()
    if lives >0:
        for position in range(length_of_choosen_word):
            letter = choosen_word[position]
            if letter == guess:
                display[position] = letter
                print(display)
        if guess not in choosen_word:
            lives -=1
            if lives ==0:
                end_of_game = True
                print("You Lost")
        if "_" not in display:
            end_of_game = True
            print("You Win")
    print(lives)


