from turtle import *
import random
from constants_art import set_theme

def draw_square(x,y,s):
    penup()
    goto(x-s/2,y-s/2)
    pendown()
    for i in range(4):
        forward(s)
        left(90)



set_theme(thickness=2)

shrink = 15
noise = 5
size = 100
for x in range(-500+size//2,500,size):
    for y in range(-500+size//2,500,size):
        draw_square(x,y,size)

        #determine the offsets
        x_off = random.uniform(-noise, noise)
        y_off = random.uniform(-noise, noise)

        for i in range(6):
            draw_square(x+i*x_off,y+i*y_off,size-i*shrink)


tracer(True)
exitonclick()