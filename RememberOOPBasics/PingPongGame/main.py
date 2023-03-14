from ball import Ball
from field import Field
from paddle import Paddle
from turtle import Screen

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor('black')
    screen.title('Ping *** Pong Mother***')
    screen.tracer(0)


   #  ball_instance = Ball()
    paddle_1 = Paddle((350, 0))
    paddle_2 = Paddle((-350, 0))


    screen.listen()
    screen.onkey(key='Up', fun=paddle_1.go_up)
    screen.onkey(key='Down', fun=paddle_1.go_down)
    screen.onkey(key='w', fun=paddle_2.go_up)
    screen.onkey(key='s', fun=paddle_2.go_down)

    game_is_on = True
    while game_is_on:
        screen.update()
    screen.exitonclick()