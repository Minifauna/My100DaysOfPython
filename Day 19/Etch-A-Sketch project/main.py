from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.bgcolor('black')
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet.', prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
positions = [-150, -100, -50, 0, 50, 100, 150]
racers = []

for x in colors:
    turtle = Turtle('turtle')
    turtle.pu()
    turtle.color(x)
    turtle.setposition(x=-230, y=positions[colors.index(x)])
    racers.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for racer in racers:
        if racer.xcor() > 230:
            is_race_on = False
            winning_color = racer.pencolor()
            if winning_color == user_bet:
                print(f'You won! The {winning_color} turtle finished first!')
            else:
                print(f'Better luck next time! The {winning_color} turtle finished first!')
        racer.fd(randint(0, 10))

screen.exitonclick()
