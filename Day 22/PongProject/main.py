from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from random import randint

game_is_on = True

screen = Screen()
screen.setup(800,600)
screen.bgcolor('black')
screen.title('PyPong')
screen.tracer(0)
scoreboard = Scoreboard()
paddle = Paddle()
screen.listen()
screen.onkey(paddle.up, 'Up')
screen.onkey(paddle.down, 'Down')

while game_is_on:
    screen.update()
    paddle.ball_movement()
    paddle.cpu_movement()
    x_cor = paddle.ball.xcor()
    y_cor = paddle.ball.ycor()
    heading = paddle.ball.heading()
    if y_cor < -390 or y_cor > 390:
        paddle.ball.setheading((heading + 90) % 360)
    if paddle.ball.distance(x=paddle.player) < 30:
        paddle.ball.setheading((heading + 180 + randint(-5, 5)) % 360)
        paddle.ball.fd(20)
    if paddle.ball.distance(x=paddle.cpu) < 30:
        paddle.ball.setheading((heading + 180 + randint(-5, 5)) % 360)
        paddle.ball.fd(20)
    if x_cor < -390:
        paddle.ball_home()
        scoreboard.update_cpu_score()
        scoreboard.refresh_midline()
    if x_cor > 390:
        paddle.ball_home()
        scoreboard.update_player_score()
        scoreboard.refresh_midline()










screen.exitonclick()