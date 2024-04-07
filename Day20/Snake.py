import turtle as t 
from turtle import Turtle
X_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180 
RIGHT = 0

class Snake:
    def __init__(self):
        '''code should define what would happen when we initialize a snake object'''
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for turtles in X_POSITIONS:
            '''it used to create new turtles'''
            self.add_segment(turtles)

    def add_segment(self,position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(x=position)
        self.segments.append(new_segment)
        
    def extend(self):
        #add new segment whenever snake hits the food
        self.add_segment(self.segments[-1].position())
        
    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            '''it used to move our snake'''
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(x=new_x,y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)