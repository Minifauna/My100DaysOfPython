import random
from art import logo
continue_playing = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand = []
player_hand = []
dealer_hand += random.choices(cards, k=2)
player_hand += random.choices(cards, k=2)
print(logo)
print(f"Dealer's shown: {dealer_hand[0]}")
print(sum(dealer_hand))
print(f"Your hand: {player_hand}")
print(sum(player_hand))
hit = input("Would you like another card? Y or N ").lower()

def round_start():
    dealer_hand = []
    player_hand = []
    dealer_hand += random.choices(cards, k=2)
    player_hand += random.choices(cards, k=2)
    print(logo)
    print(f"Dealer's shown: {dealer_hand[0]}")
    print(sum(dealer_hand))
    print(f"Your hand: {player_hand}")
    print(sum(player_hand))

def round_finish():
    while sum(dealer_hand) < 17:
        dealer_hand.append(random.choice(cards))
        print(f'Dealer hand: {dealer_hand} Dealer total: {sum(dealer_hand)}')
    else:
        if sum(dealer_hand) == 21:
            print(f'Dealer hand: {dealer_hand}')
            print(f'Your hand: {player_hand}')
            print(f'Your total: {sum(player_hand)}')
            print(f'Dealer wins with: {sum(dealer_hand)} {dealer_hand}')
        elif sum(player_hand) == 21:
            print(f'Dealer hand: {dealer_hand}')
            print(f'Your hand: {player_hand}')
            print(f'Dealer total: {sum(dealer_hand)}')
            print(f'You win with: {sum(player_hand)} {player_hand}')
        elif sum(player_hand) > 21:
            print(f'Dealer hand: {dealer_hand}')
            print(f'Your hand: {player_hand}')
            print(f'Dealer wins with: {sum(dealer_hand)}')
            print(f'You busted with: {sum(player_hand)}')
        elif sum(dealer_hand) > 21:
            print(f'Dealer hand: {dealer_hand}')
            print(f'Your hand: {player_hand}')
            print(f'Dealer busted with: {sum(dealer_hand)}')
            print(f'You win with: {sum(player_hand)}')
        elif sum(dealer_hand) > 21 and sum(player_hand) > 21:
            print(f'Dealer hand: {dealer_hand}')
            print(f'Your hand: {player_hand}')
            print('Tie game! Both bust!')
        elif sum(dealer_hand) > sum(player_hand):
            print(f'Dealer hand: {dealer_hand}')
            print(f'Your hand: {player_hand}')
            print(f'Dealer wins with: {sum(dealer_hand)}')
        elif sum(player_hand) > sum(dealer_hand):
            print(f'Dealer hand: {dealer_hand}')
            print(f'Your hand: {player_hand}')
            print(f'You win with: {sum(player_hand)}')
        elif sum(player_hand) == sum(dealer_hand):
            print(f'Dealer hand: {dealer_hand}')
            print(f'Your hand: {player_hand}')
            print('Tie game! House wins!')
    print("----------------------------------------------")

while continue_playing:
    if hit != 'y':
        round_finish()
        dealer_hand = []
        player_hand = []
        dealer_hand += random.choices(cards, k=2)
        player_hand += random.choices(cards, k=2)
        print(logo)
        print(f"Dealer's shown: {dealer_hand[0]}")
        print(sum(dealer_hand))
        print(f"Your hand: {player_hand}")
        print(sum(player_hand))
        hit = input("Would you like another card? Y or N ").lower()
    elif hit == 'y':
        player_hand.append(random.choice(cards))
        print(f'Your hand is now: {player_hand} and your total: {sum(player_hand)}')
        if (sum(player_hand) > 21) and 11 in player_hand:
            player_hand[(player_hand.index(11))] = 1
            print(f'Ace low!\nYour hand is now: {player_hand} and your total: {sum(player_hand)}')
        elif sum(player_hand) > 21 and 11 not in player_hand:
            print(f'Dealer hand: {dealer_hand}')
            print(f'Your hand: {player_hand}')
            print(f'Dealer wins with: {sum(dealer_hand)}')
            print(f'You busted with: {sum(player_hand)}')
            dealer_hand = []
            player_hand = []
            dealer_hand += random.choices(cards, k=2)
            player_hand += random.choices(cards, k=2)
            print(logo)
            print(f"Dealer's shown: {dealer_hand[0]}")
            print(sum(dealer_hand))
            print(f"Your hand: {player_hand}")
            print(sum(player_hand))
        hit = input("Would you like another card? Y or N ").lower()

