from turtle import Turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0) #stops updating the screen so need something later on to keep updating it screen.update()


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_right()
    if ball.ycor() > 285 or ball.ycor() < -285: # jo -1 * -1 ir plus un vins ies uz augsu atkal
        ball.bounce_y()

    #Detect collison with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    elif ball.xcor() >380:
        ball.reset_left()
        scoreboard.l_point()

    elif ball.xcor() < -380:
        ball.reset_left()
        scoreboard.r_point()


screen.exitonclick()
