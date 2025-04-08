from art import logo
print(logo)
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

bids = {}
def finished():
    print(f"There were {len(bids)} bids in total.")
    print(f"The winner is {max(bids, key=bids.get)} with ${bids[max(bids, key=bids.get)]}")
continue_bidding = True
while continue_bidding:
    name = str(input("\nWhat is your name?\n"))
    bid = int(input("\nWhat is your bid?\n$"))
    bids[name] = bid
    more = str(input("Are there more bids? Y or N\n").lower())
    if more == "n":
        continue_bidding = False
        finished()
    else:
        print("\n" * 100)
