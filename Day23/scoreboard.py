from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()
        
    def update_score(self):
        self.goto(0,260)
        self.write(f"Score {self.score}",align='center',font=FONT)

    def increase_score(self):
        self.clear()
        self.score+=1
        self.update_score()
    
