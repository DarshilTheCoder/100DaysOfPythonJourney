from turtle import Turtle
import random as rd

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=.5,stretch_wid=.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = rd.randint(-280,280)
        random_y = rd.randint(-280,280)
        self.goto(x=random_x,y=random_y)

    #     self.turtle = Turtle()
    #     self.create_food()
    # def create_food(self):
    #     self.turtle.shape('circle')
    #     self.turtle.penup()
    #     self.turtle.shapesize(stretch_len=.5,stretch_wid=.5)
    #     self.turtle.color('blue')
    #     self.turtle.speed('fastest')
    #     random_x = rd.randint(-280,280)
    #     random_y = rd.randint(-280,280)
    #     self.turtle.goto(x=random_x,y=random_y)

