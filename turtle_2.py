from turtle import *
import random

# initializing
clear()
pu()
goto(0,-275)
angle = 0
colormode(255)
speed = 50

# drawing
while pos():
    pu()
    angle = angle + 3
    fd(15)
    seth(angle)
    pd()
    color_r = random.randint(0,255)
    color_g = random.randint(0,255)
    color_b = random.randint(0,255)
    color(color_r,color_g,color_b)
    if (color_r + color_g + color_b)%50 == 0:
        begin_fill()
        circle(20)
        end_fill()
    else:
        circle(20)
