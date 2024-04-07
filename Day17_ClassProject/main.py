from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

Question_bank = []
for i in question_data:
    question = Question(i['text'],i['answer'])
    Question_bank.append(question)

print(Question_bank)

quiz = QuizBrain(Question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")