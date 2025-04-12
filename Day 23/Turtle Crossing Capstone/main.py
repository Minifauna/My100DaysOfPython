from time import sleep
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Turtle Py')
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkeypress(player.up, 'Up')

game_is_on = True
while game_is_on:
    sleep(0.1)
    screen.update()
    cars.move()
    for car in cars.cars:
        if car.distance(player) <= 20:
            game_is_on = scoreboard.game_over()
    if player.player.ycor() >= 280:
        player.back_to_home()
        cars.increase_speed()
        scoreboard.update_level()


screen.exitonclick()