print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# <= 18 admission is $7 // >18 admission is $12

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")

# 0-11 age is $5 // 12-18 age is $7 // 19+ age is $12


