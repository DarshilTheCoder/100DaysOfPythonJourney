from turtle import Turtle,Screen
import turtle as t 
import random as rd

tim_turtle= Turtle()
screen = Screen()

def move_forward():
    tim_turtle.forward(20)

def move_backward():
    tim_turtle.backward(20)

def counter_clockwise_dir():
    tim_turtle.right(10)

tim_turtle = Turtle()

def anti_clockwise_dir():
    tim_turtle.left(10)

def clear_drawing():
    tim_turtle.reset()
t.colormode(255)
def random_color():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    return (r,g,b)

screen.listen()
# screen.onkey(key='S',fun=creating_turtles)
screen.onkey(key='W',fun=move_forward)
screen.onkey(key='S',fun=move_backward)
screen.onkey(key='A',fun=counter_clockwise_dir)
screen.onkey(key='D',fun=anti_clockwise_dir)
screen.onkey(key='C',fun=clear_drawing)
screen.exitonclick()

