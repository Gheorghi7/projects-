import time
from tkinter import *

from quiz_brain import QuizBrain

TIME_COLOR = '#375362'


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizler')
        self.window.config(padx=20, pady=20, bg=TIME_COLOR)

        self.score_label = Label(text=f"Score: {self.score}", bg=TIME_COLOR, font=('Arial', 15, 'bold'))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')

        self.question_text = self.canvas.create_text(150, 125, text='Something', width=280,
                                                     font=('Arial', 15, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file='images/true.png')
        false_image = PhotoImage(file='images/false.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.check_true)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_image, highlightthickness=0, command=self.check_false)
        self.false_button.grid(row=2, column=1)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.configure(bg='white')
        if self.quiz.still_has_q:
            q_text = self.quiz.next_q()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end of the quiz')

    def check_true(self):
        is_right = self.quiz.check_answer('True')
        self.check_feedback(is_right)

    def check_false(self):
        is_right = self.quiz.check_answer('False')
        self.check_feedback(is_right)

    def check_feedback(self, is_answer):
        if is_answer:
            self.canvas.configure(bg='green')
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.configure(bg='red')
            print("You are not right")
        self.window.after(1000, self.next_question)
