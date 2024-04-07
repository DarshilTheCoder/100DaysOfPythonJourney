from turtle import Turtle,Screen
import turtle as t 
import random as rd


screen = Screen()
is_GameOn = False
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter your Color")
color_list = ["red",'purple','blue','green','pink','yellow']
# y_positions = [-70,-30,10,50,90,130]
all_turtles = []
y = -100

for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color_list[turtle_index])
    new_turtle.penup()
    # new_turtle.goto(x=-230,y=y_positions[turtle_index])
    new_turtle.goto(x=-230,y=y)
    y = y+50
    all_turtles.append(new_turtle)

if user_bet:
    is_GameOn = True

while is_GameOn:
    for turtle in all_turtles:
        if turtle.xcor()>=230:
            is_GameOn= False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is winner!")
            else:
                print(f"You lose! the {winning_color} turtle is winner!")
        random_dist = rd.randint(0,10)
        turtle.forward(random_dist)

screen.exitonclick()