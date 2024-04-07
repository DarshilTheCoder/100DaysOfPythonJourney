import random as rd
import string  


letters = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation

class generatePassword:
    def generatepassword(self):
        self.password_length = rd.randint(3,4)
        self.password = ""
        for i in range(0,self.password_length):
            self.password+=rd.choice(letters)
            self.password+=rd.choice(numbers)
            self.password+=rd.choice(punctuation)
        self.password_list = list(self.password)
        rd.shuffle(self.password_list)
        self.password = ''.join(self.password_list)
        return self.password