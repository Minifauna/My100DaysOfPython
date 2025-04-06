import hand
import random
hands = [hand.rock, hand.paper, hand.scissors]
hand_string = ["Rock", "Paper", "Scissors"]
player = int(input("0 for Rock, 1 for Paper, 2 for Scissors\n"))
computer = random.randint(0, 2)
if player > 2:
    print("Wrong game, buddy.")
elif 0 <= player <= 2:
    print(f"You chose {hand_string[player]}.\n{hands[player]}")
    print(f"Computer chose {hand_string[computer]}.\n{hands[computer]}")
    if computer == (player + 1) % 2:
        print("You win!")
    elif computer == player:
        print("Draw.")
    else:
        print("You lose.")
