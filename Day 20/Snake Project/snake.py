from turtle import Turtle

SNAKE_CONSTANT = 20 #movement distance and snake size are linked via this constant
UP = 90         # coordinate system translation constants
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:


    def __init__(self):
        self.snake_body = []
        self.spawn_in()
        self.head = self.snake_body[0]


    def spawn_in(self):
        for x in range(3):
            snake_seg = Turtle('square')
            snake_seg.pu()
            snake_seg.color('cyan')
            snake_seg.setposition(snake_seg.xcor() - (x * SNAKE_CONSTANT), snake_seg.ycor())
            self.snake_body.append(snake_seg)

    def add_segment(self, position):
        snake_seg = Turtle('square')
        snake_seg.pu()
        snake_seg.color('cyan')
        snake_seg.goto(position)
        self.snake_body.append(snake_seg)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def reset(self):
        for segments in self.snake_body:
            segments.goto(1000, 1000)
        self.snake_body.clear()
        self.spawn_in()
        self.head = self.snake_body[0]


    def movement(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_xcor = self.snake_body[seg_num - 1].xcor()
            new_ycor = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_xcor, new_ycor)
        self.head.fd(SNAKE_CONSTANT)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        else:
            pass

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        else:
            pass

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        else:
            pass

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        else:
            pass

