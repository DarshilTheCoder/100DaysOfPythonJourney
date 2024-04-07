#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = '[name]'
with open('./Input/Names/invited_names.txt') as namereader:
    names= namereader.readlines()
    # print(names)
with open('./Input/Letters/starting_letter.txt') as filereader:
    file_content = filereader.read()
    for name in names:
        stripped_names = name.strip()
        new_file = file_content.replace(PLACEHOLDER,stripped_names)
        # print(new_file)
        with open(f'D:/PythonProjects/PythonLearningResources/100DaysOfPythonJourney/Day24/Output/ReadyToSend/letter_for_{stripped_names}',mode="w") as writeletter:
            writeletter.write(new_file)
        