bmi = 84 / 1.65 ** 2
print(bmi)
# Prints a float due to division
print(str(bmi))
# Prints string by "flooring" the float - removing the decimal and everything after without rounding
print(round(bmi))
# Rounded up to 31, default rounds to integer
print(round(bmi, 2))
# Rounded to 2 decimal places, no longer being converted to an integer

#Assignment operators
score = 0

# User scores a point
score += 1
print(score)
# works with each mathematical operator as well

# F-strings
age = 12

print(f"I am {age} years old")

print(f"Your score is {score}")
