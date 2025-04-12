from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):


    def __init__(self):
        super().__init__()
        self.player = Turtle('turtle')
        self.player.speed('slowest')
        self.player.pu()
        self.player.color('cyan')
        self.player.setheading(90)
        self.back_to_home()


    def up(self):
        self.player.fd(MOVE_DISTANCE)

    def back_to_home(self):
        self.player.teleport(*STARTING_POSITION)
