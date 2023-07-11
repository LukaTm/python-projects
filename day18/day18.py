from turtle import Turtle, Screen ,colormode , pencolor
import random


timmy = Turtle()
screen = Screen()
timmy.speed('fastest')
for x in range(72):
    timmy.circle(radius=150)
    timmy.left(5)

def draw_spireograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spireograph(10)

screen.exitonclick()