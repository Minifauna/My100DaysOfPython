import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def password_generator():
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    gen_pass = []
    counter1 = 0
    counter2 = 0
    counter3 = 0
    for lett in letters:
        gen_pass.append(random.choice(letters))
        counter1 += 1
        if counter1 >= int(nr_letters):
            break
    for symb in symbols:
        gen_pass.append(random.choice(symbols))
        counter2 += 1
        if counter2 >= int(nr_symbols):
            break
    for numb in numbers:
        gen_pass.append(random.choice(numbers))
        counter3 += 1
        if counter3 >= int(nr_numbers):
            break
    random.shuffle(gen_pass)
    password = ''.join(gen_pass)
    print(f"Suggested password: {password}")
    return another_password()

def another_password():
    while True:
        another = str(input("Would you like to generate another password? 'Y' or 'N'\n"))
        if another not in {"Y", "N"}:
            print("Invalid input.")
        elif another == "N":
            print("Thank you, goodbye.")
            break
        elif another == "Y":
            return password_generator()
password_generator()
