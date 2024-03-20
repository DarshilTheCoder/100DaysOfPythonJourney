#Day9 learning is about dictonaries and nesting and going to make project

dict = {
    #key is provided in a double or single quotes only otherwise it will consider a variable 
    "name":'darshil',
    "number":123,
    'loop':'it is loop'
}

print(dict["name"]) #key is provided 
print(dict['number'])

dict["function"]="this is function" # this way we can add new key value pair
print(dict)
print(dict['function'])

# this is called nesting dictonary
dict["anotherDict"]={
    "name2": 'darshil2',
    "number2":345
}

for key in dict:
    print(key) # so in for loop it will return only the key and not value 
    print(dict[key]) # inorder to get value we have to provide key to dict 

print(dict)
# dict={}
# print(dict)
dict['list']=['apple,banana,mango'] # hence we can add anything to dictonaries 
print(dict)
print(dict['list'])

#dict into dict and have list and key value pair
travel_log1 = {
    'France':{'cities_visited':['PARIS,lille'],'total_visits':12},
    'Germany':{'cities_visited':['berlin,hamburg'],'total_visits':2}
}

#make a list of dict 
travel_log2 = [
    {'country':'France',
    'cities_visited':['PARIS,lille'],
    'total_visits':12
    },
    {'country':'Germany',
    'cities_visited':['berlin,hamburg'],
    'total_visits':2
    }
]

print(travel_log1)
print(travel_log2)

#Day9 Project is Biding Auction software
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

bid={}
def add_bid_values(name,bid_value):
    bid[name]=bid_value

auction_on = True
while auction_on:
    name = input("enter your name = ")
    bid_value = int(input("enter your bid value = "))
    add_bid_values(name,bid_value)
    question = input("is anyother person? type yes or no = ")
    if question == 'yes':
        clear_screen()
    else:
        auction_on = False

max_bid = 0
winner_name = ""
for key in bid:
    if bid[key]>max_bid:
        max_bid = bid[key]
        winner_name = key

# print(bid)
print(f'winner name is {winner_name} with {max_bid} ')


