name = str(input("\nWhat is your name?\n"))
bid = int(input("\nWhat is your bid?\n$"))
more = str(input("Are there more bids? Y or N\n").lower())
bids = {}
bids[name] = bid
def finished():
    print(f"There were {len(bids)} bids in total.")
    print(f"The winner is {max(bids)} with ${bids[max(bids)]}")
if more == "y":
    bids[name] = bid
    again = str(input("Are there more bids? Y or N\n").lower())
    if again == "y":
        bids[name] = bid
        name = str(input("\nWhat is your name?\n"))
        bid = int(input("\nWhat is your bid?\n$"))
    else:
        finished()

