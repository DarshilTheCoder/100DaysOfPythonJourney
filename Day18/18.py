#Day18 Challenges about turtle graphics
from turtle import Turtle, Screen
import turtle as t
import random
timmy_turtle = Turtle()
def exit_on_click():
    screen = Screen()
    screen.exitonclick()
def turtle_specs():
    timmy_turtle.shape('turtle')
    # timmy_turtle.color('red','green')
# Challenge 1: Draw a square
# def draw_square():
#     turtle_specs()
#     for i in range(4):
#         timmy_turtle.forward(100)
#         timmy_turtle.right(90)
#     exit_on_click()
    
# draw_square()

# Challenge 2: Draw a dashed lines
# def draw_dashed_lines():
#     turtle_specs()
#     timmy_turtle.pos
#     for i in range(10):
#         timmy_turtle.forward(10)
#         timmy_turtle.penup()
#         timmy_turtle.forward(10)
#         timmy_turtle.pendown()
    
#     exit_on_click()

# draw_dashed_lines()
    
#Challenge 3: Draw different shapes

# def square(angle,y):
#     for x in range(4):
#         timmy_turtle.color('blue')
#         timmy_turtle.forward(100)
#         timmy_turtle.right(float(angle/y))
# def pentagon(angle,y):
#     for x in range(5):
#         timmy_turtle.color('green')
#         timmy_turtle.forward(100)
#         timmy_turtle.right(float(angle/y))
# def hexagon(angle,y):
#     for x in range(6):
#         timmy_turtle.color('pink')
#         timmy_turtle.forward(100)
#         timmy_turtle.right(float(angle/y))
# def heptagon(angle,y):
#     for x in range(7):
#         timmy_turtle.color('black')
#         timmy_turtle.forward(100)
#         timmy_turtle.right(float(angle/y))
# def octagon(angle,y):
#     for x in range(8):
#         timmy_turtle.color('yellow')
#         timmy_turtle.forward(100)
#         timmy_turtle.right(float(angle/y))
# def nonagon(angle,y):
#     for x in range(9):
#         timmy_turtle.color('purple')
#         timmy_turtle.forward(100)
#         timmy_turtle.right(float(angle/y))
# def decagon(angle,y):
#     for x in range(10):
#         timmy_turtle.color('orange')
#         timmy_turtle.forward(100)
#         timmy_turtle.right(float(angle/y))

# def different_shapes():
#     turtle_specs()
#     angle = 360.0
#     for x in range(3):
#         timmy_turtle.color('red')
#         timmy_turtle.forward(100)
#         timmy_turtle.right(float(angle/3))
#     square(angle,4)
#     pentagon(angle,5)
#     hexagon(angle,6)
#     heptagon(angle,7)
#     octagon(angle,8)
#     nonagon(angle,9)
#     decagon(angle,10)
#     exit_on_click()

# different_shapes()

#Challenge 4: Draw a random walk
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

# directions =[0,90,180,270]

# timmy_turtle.width(5)
timmy_turtle.speed('fastest')
# for _ in range(100):
#     turtle_specs()
#     color_tuple = random_color()
#     timmy_turtle.color(color_tuple)
#     timmy_turtle.forward(40)
#     timmy_turtle.setheading(random.choice(directions))


#Challenge 5: Draw a spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy_turtle.color(random_color())
        timmy_turtle.circle(50)
        # timmy_turtle.left(5)
        timmy_turtle.setheading(timmy_turtle.heading()+size_of_gap)
    exit_on_click()
draw_spirograph(5)




