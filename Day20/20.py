#Day20 Snake game project
import turtle as t 
from turtle import Screen
import random as rd
import time 
from Snake import Snake #inorder to import class you have take it from file 
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.setup(width=600,height=600)
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

is_game_on = True


while is_game_on:
    screen.update()
    time.sleep(.1)
    # for seg in segments:
        # seg.forward(10) #the working of for loop in python is totally different here you can run for loop on list where each of items will get iterable and you can apply the changes on each item
    snake.move()
    #used to increase the score
    if snake.head.distance(food) < 15:
        scorecard = scoreboard.increase_score()
        snake.extend()
        food.refresh()
    #used to detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        is_game_on = False
        scoreboard.reset()
        scoreboard.game_over()
    #used to detect the collision with tail
    for segments in snake.segments[1:]:
        if snake.head.distance(segments)<10:
            is_game_on = False
            scoreboard.reset()
            scoreboard.game_over()

screen.exitonclick()