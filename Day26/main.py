# Keyword Method with iterrows()
# {new_key:new_row for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
import pandas as pd 
csv_file_reader = pd.read_csv('nato_phonetic_alphabet.csv')
nato_data = pd.DataFrame(csv_file_reader)
nato_dict = {row.letter:row.code for (index,row) in nato_data.iterrows()}
# print(nato_dict)

#Another way of making required dict()
# data = pd.read_csv('nato_phonetic_alphabet.csv')
# data.to_dict()
# phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}

is_game_on = True
while is_game_on:
    try:
        user_input = input('Please enter a word = ').upper()
        # list_of_words =[]
        # for letter in user_input:
        #     if letter in nato_dict:
        #         new_word = nato_dict[letter]
        #         list_of_words.append(new_word)
        # print(list_of_words)
        list_of_new_words = [nato_dict[letter] for letter in user_input]
        print(list_of_new_words)
        asking = input('Want to play more? Type "yes" else "no"').lower()
        if asking == 'no':
            is_game_on = False
    except KeyError:
        print('Sorry, only letters in the alphabet please')