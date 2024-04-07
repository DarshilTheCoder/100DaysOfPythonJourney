#Day30 of Learning Python 
#Going to understand about try,except,else and finally keywords which is used in exception handling

try:
    file = open('data.txt')
    a_dict = {'key':'value'}
    #now when KeyError handler is not mentioned so it just passed this error and move to except block Now want to avoid such situation then create all types of error handler
    # print(a_dict['key'])
    fruits = ['apple','banana']
    print(fruits[2])
    
except (FileNotFoundError,KeyError,IndexError,TypeError) as error_message:
    #this way we can save our app from crashing and also we get to know about which type of error is occuring 

    file = open('data.txt',mode='w')
    file.write('something new is added')
    print(f"{error_message}")
else:
    #this block will execute only after TRY block , if python goes into except block then else block will not execute
    content = file.read()
    print(content)
    print('hello')
finally:
    file.close()
    print('finaaly is printing No matter what happens above')
    
#We can raise our OWN ERROR also 
height = float(input("enter your height= "))
weight = int(input("enter your weight = "))

if height>3:
    raise ValueError("Height should not be greater than 3 !!!")

bmi = weight/height**2
print(bmi)

#Go to Day29 where we are learning about JSON methods 
#json.loads() method is used to read the json data and convert it into DICT
#json.dump() is used to write a data into file in a json format 
#json.update() is used to update the current data but for that first have to read then update then dump it into file