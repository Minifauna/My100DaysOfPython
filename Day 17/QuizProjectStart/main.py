from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for x in question_data:
    text = x.get('question')
    answer = x.get('correct_answer')
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print("You've completed the quiz!\n")
print(f'Final score: {quiz.correct_answers}/{quiz.question_number}')
