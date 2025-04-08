print("Welcome to the tip calculator!")
# Greetings
bill = float(input("What was the total bill? XXX,XXX.XX : $"))
tip = int(input("What percentage tip would you like to give? XX : "))
people = int(input("How many people to split the bill? "))
# Gathering variables
split = format(round(((bill*(1+(tip/100)))/people), 2),'.2f')
# Formatting a rounded equation to 2 decimal places
print(f"Each person should pay: ${split}")
# Print result
