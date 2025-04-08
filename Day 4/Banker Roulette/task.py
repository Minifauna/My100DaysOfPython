import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_number = random.randint(0, 4)
print(f"{friends[random_number]} is paying this time!")
# random.choice example
print(f"{random.choice(friends)} is paying this time!")
