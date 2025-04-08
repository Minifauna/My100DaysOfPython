print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
# then check this if statement, "photo" is independent of "age"
    photo = input("Would you like a photo taken? Y for yes // N for no: ")
    if photo == "y":
        bill += 3 #add $3 to the bill

    print(f"Your bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
