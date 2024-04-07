import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
ALIGN = 'center'
FONT = ('Arial',20,'normal')
player = Player()
car_manager= CarManager()
score = Scoreboard()
screen.onkey(fun=player.moveup,key="Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.creating_cars()
    car_manager.move_cars()
    #detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            car_manager.goto(x=0,y=0)
            car_manager.write(f"Game Over",align=ALIGN,font=FONT)
            car_manager.goto(x=0,y=-50)
            car_manager.write(f"You Collide with Car! Your Score is {score.score}",align=ALIGN,font=FONT)
            game_is_on = False
    
    #detect when it reaches to finish line and increasing the speed and score
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.levelup()
        score.increase_score()
screen.exitonclick()
