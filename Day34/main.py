from question_model import Question
from data import QuestionData
from quiz_brain import QuizBrain
from ui import GraphicalInterface

question_bank = []
questionData = QuestionData()
question_data = questionData.get_question()
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)



quiz = QuizBrain(question_bank)
interface = GraphicalInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()
#here we have comment out the above code because it is the interface class have mainloop() which will get confuse if there is another while loop is there


