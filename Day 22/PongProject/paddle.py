from turtle import Turtle
from random import choice

SPAWN_DIRECTION = [0, 5, 175, 180, 185, 355]
POSITIONS = [(-375,0), (375,0)]
PADDLE_SPEED = 40
BALL_SPEED = 0.4 # scale of 0.1 to 1.0 with 1.0 being 'impossible'
CPU_SPEED = ['slowest', 'slow', 'normal', 'fast', 'fastest']
CPU_DIFFICULTY = 3 # scale of 0-4 with 4 being 'impossible'


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.paddles = []
        self.balls = []
        self.spawn_paddles()
        self.player = self.paddles[0]
        self.cpu = self.paddles[1]
        self.cpu.speed(CPU_SPEED[CPU_DIFFICULTY])
        self.ball_spawn()
        self.ball = self.balls[0]


    def ball_spawn(self):
        ball = Turtle('circle')
        ball.color('white')
        ball.shapesize(.5, .5)
        ball.pu()
        ball.setheading(choice(SPAWN_DIRECTION))
        self.balls.append(ball)

    def ball_movement(self):
        self.ball.fd(BALL_SPEED)

    def ball_home(self):
        self.ball.home()
        self.ball.setheading(choice(SPAWN_DIRECTION))

    def spawn_paddles(self):
        for position in POSITIONS:
            new_paddle = Turtle('square')
            new_paddle.color('cyan')
            new_paddle.pu()
            new_paddle.shapesize(3,0.5)
            new_paddle.teleport(*position)
            self.paddles.append(new_paddle)

    def cpu_movement(self):
        if self.ball.ycor() != self.cpu.ycor():
            target = self.ball.ycor() - self.cpu.ycor()
            self.cpu.sety(target*0.9)


    def up(self):
        self.player.sety(self.player.ycor() + PADDLE_SPEED)

    def down(self):
        self.player.sety(self.player.ycor() - PADDLE_SPEED)

