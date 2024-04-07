from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(x=x_cor,y=y_cor)
        # self.initial_r_paddle_position = (350,0)
        # self.initial_l_paddle_position = (-350,0)
        
        
    def movingup(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(),y=new_y)
    def movingdown(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(),y=new_y)