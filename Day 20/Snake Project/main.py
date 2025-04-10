from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from time import sleep

NEG_BOUND = -290
POS_BOUND = 290

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

play_game = True
while play_game:
    screen.update()
    sleep(0.1)
    snake.movement()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()
    # detect collision with wall
    if snake.head.xcor() > POS_BOUND or snake.head.xcor() < NEG_BOUND or snake.head.ycor() > POS_BOUND or snake.head.ycor() < NEG_BOUND:
        play_game = False
        scoreboard.game_over()
    # detect collision with tail
    for segments in snake.snake_body[1:]:
        if snake.head.distance(segments) < 10:
            play_game = False
            scoreboard.game_over()

screen.exitonclick()
