from turtle import Turtle
from car_manager import CarManager
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.go_to_start()
    
    def moveup(self):
        self.forward(MOVE_DISTANCE)
        
    def is_at_finish_line(self):
        if self.ycor()>=FINISH_LINE_Y:
            return True
        
    def go_to_start(self):
        self.goto(STARTING_POSITION)
            
