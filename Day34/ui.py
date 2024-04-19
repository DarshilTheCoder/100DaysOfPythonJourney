from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class GraphicalInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.question_number = 0
        self.windows = Tk()
        self.windows.title('Quizzler')
        self.windows.config(background=THEME_COLOR,width=500,height=1000,padx=20,pady=20)
        
        self.scoreBoard = Label(text='Score : 0',foreground='white',background=THEME_COLOR,font=('Arial',15,'italic'))
        self.scoreBoard.grid(row=0,column=1)
        
        self.canvas = Canvas(width=300,height=250,background='white',highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125,text='Some Question Text',font=('Arial',15,'italic'),fill=THEME_COLOR,width=250)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        
        true_img = PhotoImage(file='./images/true.png')
        self.true_btn = Button(image=true_img,highlightthickness=0,background=THEME_COLOR,command=self.answering_true)
        self.true_btn.grid(row=2,column=0)
        
        false_img = PhotoImage(file='./images/false.png')
        self.false_btn = Button(image=false_img,highlightthickness=0,background=THEME_COLOR,command=self.answering_false)
        self.false_btn.grid(row=2,column=1)
        
        #here everything is ahead of self except the images coz after self it becomes property which we can use anywhere in a class but images are not going to use
        
        self.get_next_question()
        
        self.windows.mainloop()
        
    def get_next_question(self):
        self.canvas.config(background='white')
        if self.question_number>=10:
            self.canvas.itemconfig(self.question_text,text = f"Thank you for Playing\n Your final Score:{self.score}")
        else:
            q_text= self.quiz.next_question()
            self.question_number+=1
            self.canvas.itemconfig(self.question_text,text =q_text)
    
    def answering_true(self):
        user_input = 'True'
        answer = self.quiz.check_answer(user_answer=user_input)
        self.give_feedback(right_answer=answer)
        
    def answering_false(self):
        user_input = 'False'
        answer = self.quiz.check_answer(user_answer=user_input)
        self.give_feedback(right_answer=answer)
        
    def give_feedback(self,right_answer):
        if right_answer:
            self.canvas.config(background='green')
            self.score+=1
            self.scoreBoard.config(text=f'Score:{self.score}')
        else:
            self.canvas.config(background='red')
        self.windows.after(1000,self.get_next_question)
        
        
    