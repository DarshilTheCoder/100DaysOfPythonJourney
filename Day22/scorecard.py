from turtle import Turtle
class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        
    def update_score(self):
        self.goto(-100,240)
        self.write(f"{self.l_score}",align='center',font=('Arial',40,'normal'))
        self.goto(100,240)
        self.write(f"{self.r_score}",align='center',font=('Arial',40,'normal'))

    def increase_right_paddle_score(self):
        self.clear()
        self.r_score+=1
        self.update_score()
    def increase_left_paddle_score(self):
        self.clear()
        self.l_score+=1
        self.update_score()
        