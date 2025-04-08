import random
from art import logo
from art import vs
from game_data import data
def answer_check(a_choice_pass, b_choice_pass, score):
    """Compare answer to guess, if correct - increase score and correct guess becomes a_choice, if incorrect - game over"""
    answer = "a" if a_choice_pass['follower_count'] > b_choice_pass['follower_count'] else "b"
    print(answer)
    guess = input('Who has more Instagram followers, type "A" or "B": ').lower()
    if guess == answer:
        score += 1
        a_choice = a_choice_pass if a_choice_pass['follower_count'] > b_choice_pass['follower_count'] else b_choice_pass
        b_choice = data[(random.randint(1, 50))%len(data)]
        if a_choice == b_choice:
            b_choice = data[random.randint(1, 50)]
        print('\n' * 20)
        print(logo)
        print(f'Great job! Your score is now {score}')
        print(len(data))
        print(f'Compare A: {a_choice['name']}, a {a_choice['description']}, from {a_choice['country']}.')
        print(vs)
        print(f'Against B: {b_choice['name']}, a {b_choice['description']}, from {b_choice['country']}.')
        answer_check(a_choice, b_choice, score)
    else:
        print('Incorrect.\nRefresh to try again.')
def game():
    score = 0
    a_choice_index = random.randint(1, 50)
    b_choice_index = (a_choice_index + 2)%len(data)
    a_choice = data[a_choice_index]
    b_choice = data[b_choice_index]
    print(logo)
    print(f'Compare A: {a_choice['name']}, a {a_choice['description']}, from {a_choice['country']}.')
    print(vs)
    print(f'Against B: {b_choice['name']}, a {b_choice['description']}, from {b_choice['country']}.')
    answer_check(a_choice, b_choice, score)
game()
