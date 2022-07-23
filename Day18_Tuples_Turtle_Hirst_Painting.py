import random
import turtle
from random import randint, choice
from turtle import Turtle, Screen
from data import COLORS

# CREATE A TURTLE
tim = Turtle()
tim.shape('turtle')
tim.color('coral')

# MAKING TURTLE DO THINGS
# TODO 1 : DRAW A SQUARE
for _ in range(4):
    tim.right(90)
    tim.forward(100)

# TODO 2 : DRAW A DASHED LINE

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

# TODO 3 : DRAW MULTIPLE SHAPES

for i in range(3, 11):
    tim.pencolor(random.choice(COLORS))
    j = 0
    while j < i:
        tim.forward(100)
        tim.right(360 / i)
        j += 1

# TODO 4 : DRAW RANDOM WALK
import turtle

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


tim.pensize(10)
tim.speed("fastest")

directions = [0, 90, 180, 270]
for i in range(1, 100):
    tim.pencolor(random_color())
    tim.forward(30)
    tim.right(random.choice(directions))

# TODO 5 : DRAW A SPIROGRAPH

current_angle = 0
tim.pensize(1)
while current_angle < 360:
    tim.pencolor(random_color())
    tim.circle(100)
    tim.left(5)
    current_angle += 5


# TODO PROJECT 1 : EXTRACT COLORS FROM HIERST SPOT PAINTING
import colorgram

colors = colorgram.extract('Hirst Spot Painting.jpg', 42)
lst = []
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    lst.append((r, g, b))
print(lst)
turtle.colormode(255)
tim.hideturtle()
color_list = [(239, 236, 238), (239, 237, 235), (235, 237, 242), (227, 237, 231), (28, 108, 162), (190, 40, 82),
              (232, 160, 58), (232, 214, 89), (220, 138, 174), (140, 109, 58), (107, 192, 214), (22, 57, 130),
              (208, 77, 95), (200, 167, 34), (235, 89, 53), (120, 191, 144), (13, 150, 89), (143, 208, 224),
              (107, 108, 196), (11, 184, 176), (136, 30, 72), (97, 51, 37), (6, 3, 2), (25, 157, 205), (227, 170, 187),
              (148, 214, 196), (175, 185, 220), (232, 174, 164), (23, 29, 50), (30, 91, 94), (2, 0, 1), (242, 201, 7),
              (28, 97, 94), (0, 2, 1), (80, 61, 47)]

new_y = -250
for j in range(10):
    tim.penup()
    tim.goto(-250, new_y)
    tim.pendown()
    new_y += 50
    for i in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)

my_screen = Screen()
my_screen.exitonclick()
