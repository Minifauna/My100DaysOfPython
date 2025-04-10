import turtle as t
from random import choice
# from colorgram import extract
# IMAGE = 'image.jpg'
# colors = extract(IMAGE, 10)
# color_list = []
# for x in range(len(colors)):
#     color_list.append((colors[x].rgb.r, colors[x].rgb.g, colors[x].rgb.b))
screen = t.Screen()
screen.colormode(255)
tim = t.Turtle()
tim.pu()
tim.hideturtle()
tim.teleport(-250, -250)
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (255, 0, 255), (124, 252, 0), (0, 255, 255)]
for x in range(10):
    for y in range(10):
        tim.dot(20, choice(color_list))
        tim.teleport(tim.xcor() + 50, tim.ycor())
    tim.teleport(-250, tim.ycor() + 50)
screen.exitonclick()
