import html

import data


class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.score = 0
        self.question_list = q_list

    def still_has_q(self):
        if self.question_num < len(self.question_list):
            return True
        else:
            return False

    def next_q(self):
        current_q = self.question_list[self.question_num]
        self.question_num += 1
        question_text = html.unescape(current_q.text)
        return f"Q{self.question_num} :{question_text}"

    def check_answer(self, u_answer):
        correct_answer = data.question_data[self.question_num]['correct_answer']
        if u_answer == correct_answer:
            return True
        else:
            return False


