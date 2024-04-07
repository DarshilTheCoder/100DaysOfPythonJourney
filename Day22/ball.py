from turtle import Turtle
import random as rd

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = rd.randint(-20,20)
        self.y_move = rd.randint(-20,20)
        self.moveball_speed = 0.1
        
    def moveball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x,y=new_y)
    
    def detect_collision_withwall(self):
        self.y_move*=-1
    def detect_collision_with_paddle(self):
        self.x_move*=-1
        self.moveball_speed*=0.9
            
            
            
        