from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(1,1)
        self.penup()
        self.x_move = 2
        self.y_move = 2
        self.move_speed = 0.02

    def move_right(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    def move_left(self):
        new_x = self.xcor() - self.x_move
        new_y = self.ycor() - self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9
    def bounce_x(self):
        self.x_move *=-1
    def reset_right(self):
        self.speed('fastest')
        self.goto(0,0)


    def reset_left(self):
        self.speed('fastest')
        self.goto(0, 0)
        self.bounce_x()













