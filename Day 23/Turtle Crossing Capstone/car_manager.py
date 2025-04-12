from turtle import Turtle
from random import choice, randrange

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):


    def __init__(self):
        super().__init__()
        self.cars = []
        self.speed = 5
        self.max_x = 300
        self.spawn_cars()


    def spawn_cars(self):
        for x in range(20):
            car = Turtle('square')
            car.speed('slowest')
            car.pu()
            car.shapesize(1, 2)
            car.setheading(180)
            car.color(choice(COLORS))
            car.teleport(self.max_x, randrange(-220, 220, 20))
            self.cars.append(car)
            self.max_x += 40
            if self.max_x >= 1100:
                self.max_x = 300


    def move(self):
        for car in self.cars:
            car.fd(self.speed)
            if car.xcor() <= -400:
                car.teleport(self.max_x, randrange(-220, 220, 20))
                car.color(choice(COLORS))



    def increase_speed(self):
        self.speed += MOVE_INCREMENT
