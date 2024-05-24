from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_blank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text,question_answer)
    question_blank.append(new_question)

quiz = QuizBrain(question_blank)
quiz_interface = QuizInterface(quiz)

while quiz.still_has_q():
    quiz.next_q()




