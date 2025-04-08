def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing? iterating through a sequence from 1 to 20
# 2. When is the function meant to print "You got it"? if a value in the iterable is 20
# 3. What are your assumptions about the value of i? it shouldn't reach 20 because "range" stops before the final number
