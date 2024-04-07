from turtle import Turtle,Screen
ALIGNMENT ='center'
FONT = ('Arial',20,'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_of_game = 0
        self.highScore = self.high_score()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x=0,y=270)
        self.update_score()

    
    def high_score(self):
        with open('data.txt',mode='r') as highScoreReadFile:
            return int(highScoreReadFile.read())
        
    def reset(self):
        if self.score_of_game > self.highScore:
            self.highScore = self.score_of_game
            with open('data.txt',mode='w') as highScoreWriteFile:
                highScoreWriteFile.write(str(self.highScore))
        self.score_of_game = 0
        self.update_score()

    def game_over(self):
        self.goto(x=0,y=0)
        self.write('Game Over',align=ALIGNMENT,font=FONT)

    def update_score(self):
        self.clear()
        self.write(f'Score = {self.score_of_game} High Score = {self.highScore}',align=ALIGNMENT,font=FONT)

    def increase_score(self):
            self.score_of_game+=1
            self.update_score()


        


