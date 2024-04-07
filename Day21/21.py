# from Day20_SnakeGame1Project.Snake import Snake

#Class Inheritance 

class Animal:
    def __init__(self):
        self.num_of_eyes = 2
    def breathe(self):
        print('inhale,exhale')

class Fish(Animal):
    def __init__(self):
        super().__init__() #call to super() initializer is recomended but not strictly required

    def breathe(self):
        super().breathe()
        print('doing under water')
    
    def swim(self):
        print('moving in water')

nemo = Fish()
nemo.breathe()
nemo.swim()
print(nemo.num_of_eyes)
    
class Car:
    def __init__(self):
        self.num_of_doors = 4
        self.num_of_tyres = 4
    
    def moving(self,car_name):
        print(f'{car_name} is moving at a speed of 120km/hr')


class audi(Car): 
    def __init__(self):
        super().__init__() #each and everything is inherited from parent class
    
    def moving(self, car_name): #also you can change parent method for specific child 
        super().moving(car_name)
        print(f'{car_name} is so awesome car')

class thar(Car):
    def __init__(self):
        super().__init__()
        self.num_of_doors= 5 #you can change the initializer also.
Audi = audi()
Audi.moving('audi')
Thar = thar()
print(Thar.num_of_doors)