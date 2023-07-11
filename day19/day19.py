from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def turn_left():
    tim.left(5)

def turn_right():
    tim.right(5)

def clear():
    tim.clear()



screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.onkey(key='a',fun=turn_left)
screen.onkey(key='d',fun=turn_right)
screen.onkey(key='c',fun=clear)





screen.exitonclick()
