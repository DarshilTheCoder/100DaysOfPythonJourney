#unlimitedargs

#Unlimited Positional Arguments (*args)
def add(*args):
    sum = 0
    for n in args:
        sum = sum + n
    return sum

addSum = add(1,2,3,4,5,6,7)
print(addSum)

#Many Keyword Arguments (**kwargs)
# def calculate(**kwargs): it is simple Many Keyword Arguments
def calculate(n,**kwargs): #It is postional as well as Many Keyword Arguments
    print(kwargs)
    # for (key,value) in kwargs.items():
        # print(key)
        # print(value)
    n+=kwargs['add']
    n*=kwargs['multiply']
    print(n)

calculate(2,add=3,multiply=5)

#Creating our own class contains optional arguments
class Car:
    def __init__(self,**kwargs):
        # self.model = kwargs['model']
        # self.make = kwargs['make']
        
        #we should try to use below one coz if we use above one and if we couldn't write a make in object then our program wil crash 
        self.model= kwargs.get('model')
        self.make = kwargs.get('make')

        #so while using *args we understand that here it will make tuple whose indices must be int and we can access using index value and here position wil mattter that's why we use **kwargs 
        # self.model = kwargs[0]
        # self.make = kwargs[1]
my_car = Car(model='GTR')
print(my_car.model)