try:
    age = int(input('How old are you?'))
except ValueError:
    print('Invalid input, please use numerical input. i.e. "14"')
    age = int(input('How old are you?'))
if age >= 18:
    print(f'You can drive at age {age}.')
elif age < 18:
    print(f'You cannot drive at age {age}.')
