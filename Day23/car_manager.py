from turtle import Turtle
import random as rd
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def creating_cars(self):
        random_chance = rd.randint(1,6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.color(rd.choice(COLORS))
            new_car.shapesize(stretch_wid=1,stretch_len=3)
            new_car.penup()
            random_y = rd.randint(-240,240)
            new_car.goto(x=300,y=random_y)
            self.all_cars.append(new_car)
        
    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)
            
    def levelup(self):
        self.car_speed+= MOVE_INCREMENT