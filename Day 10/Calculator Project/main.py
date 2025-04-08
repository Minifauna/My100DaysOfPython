from art import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# my_favorite_operation = add #function is triggered with parenthesis for inputs, use without to assign variable
# print(my_favorite_operation(2, 3)) #function has been reassigned

# TODO add these 4 functions into a dictionary as the values. keys = + - * /

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary

# print(operations["*"](4, 8)) # dictionary[key](n1, n2 *for function stored at [key]*)
def calculator():
    print(logo)
    use_calc = True
    num1 = float(input("Input first number: "))
    while use_calc:
        operand = input("Input operator + - * or / : ")
        num2 = float(input("Input second number: "))
        answer = operations[operand](n1=num1, n2=num2)
        print(f"The result is {num1} {operand} {num2} = {answer}\n")
        again = input(f"Retain {answer}?").lower()
        if again == "y":
            num1 = answer
        else:
            calculator()
calculator()
# while loop work perfectly well, but recursive function call provides easier to understand loop in this use case