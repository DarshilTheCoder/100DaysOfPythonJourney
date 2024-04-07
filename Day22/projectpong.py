#Day22 Going to create a project game name is PING PONG
from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scorecard import Scorecard
import time

screen = Screen()
paddle = Turtle()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)
ALIGN = 'center'
FONT = ('Arial',20,'normal')

#all class instance is created here
r_paddle = Paddle(x_cor=350,y_cor=0)
l_paddle = Paddle(x_cor=-350,y_cor=0)
ball = Ball()
score = Scorecard()

#key function in defined here
screen.onkey(fun=r_paddle.movingup,key="Up")
screen.onkey(fun=r_paddle.movingdown,key="Down")
screen.onkey(fun=l_paddle.movingup,key="w")
screen.onkey(fun=l_paddle.movingdown,key="s")
screen.onkey(fun=l_paddle.movingup,key="W")
screen.onkey(fun=l_paddle.movingdown,key="S")

is_game_on = True
while is_game_on:
    time.sleep(ball.moveball_speed)
    ball.moveball()
    #detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.detect_collision_withwall()

    #detect collision with paddle and increasing score on collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor()>340:
        ball.detect_collision_with_paddle()
        score.increase_right_paddle_score()
        score.update_score()
    if  ball.distance(l_paddle) < 50 and ball.xcor()<-340:
        ball.detect_collision_with_paddle()
        score.increase_left_paddle_score()
        score.update_score()
    
    #detect when ball misses the paddle
    if ball.xcor()<-350 or ball.xcor()>350:
        ball.hideturtle()
        ball.goto(x=0,y=0)
        ball.write("Game Over" ,align=ALIGN,font=FONT)
        if score.l_score == score.r_score:
            ball.goto(x=0,y=-50)
            ball.write(f"Game is DRAW with score {score.l_score}",align= ALIGN,font=FONT)
        elif score.l_score > score.r_score:
            ball.goto(x=0,y=-50)
            ball.write(f"Left Person win the Game with score of {score.l_score}",align= ALIGN,font=FONT)
        else:
            ball.goto(x=0,y=-50)
            ball.write(f"Right Person win the Game with score of {score.r_score}",align=ALIGN,font=FONT)
        ball.goto(x=0,y=-100)
        ball.write(f"Thank You for Playing PingPong Game",align=ALIGN,font=FONT)
        is_game_on = False
    screen.update()
screen.exitonclick()