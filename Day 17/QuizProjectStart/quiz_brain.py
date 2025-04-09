class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.correct_answers = 0

    def still_has_question(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        n_q_object = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {n_q_object.text} T or F?: ')
        self.check_answer(user_answer, n_q_object.answer[0])

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.correct_answers += 1
            print('You got it right!')
        print(f'The correct answer was: {correct_answer}.')
        print(f'Your current score is: {self.correct_answers}/{self.question_number}\n')
