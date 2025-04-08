import random
# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5
#
# def set_difficulty():
#     level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
#     if level == "easy":
#         return EASY_LEVEL_TURNS
#     else:
#         return HARD_LEVEL_TURNS
#
# def check_answer(user_guess, actual_answer, guesses):
#     if user_guess > actual_answer:
#         print('Too high.')
#         return guesses - 1
#     elif user_guess < actual_answer:
#         print('Too low.')
#         return guesses - 1
#     else:
#         print(f"You got it! The answer was {actual_answer}.\nRefresh to try again.")
#
# def game():
#     print('Number guessing game\n')
#     print(f'Guess a number between 1 and 100 (inclusive)')
#     turns = set_difficulty()
#     answer = random.randint(1, 100)
#     guess = 0
#     while guess != answer:
#         print(f'You have {turns} guess remaining.')
#         guess = int(input("Pick a number: "))
#         turns = check_answer(guess, answer, turns)
#         if turns == 0:
#             print(f'No guess remaining, the answer was: {answer}\n Refresh to try again.')
#             return
#
# game()

print('Number guessing game\n')
print(f'Guess a number between 1 and 100 (inclusive)')
lives = 10
continue_playing = True
difficulty_selection = input('Easy or Hard game?').lower()
if difficulty_selection != 'easy':
    lives = 5
answer = random.randint(1,100)
guess = int(input("Pick a number: "))
while continue_playing and lives > 1:
    if guess == answer:
        print(f'You win! You correctly guessed {answer}\n Refresh to play again.')
    elif guess > answer:
        lives -= 1
        print(f'Too high, {lives} guesses remain.\n')
        guess = int(input("Pick a number: "))
    elif guess < answer:
        lives -= 1
        print(f'Too low, {lives} guesses remain.\n')
        guess = int(input("Pick a number: "))
else:
    print(f'No guess remaining, the answer was: {answer}\n Refresh to try again.')
    continue_playing = False
