from ball import Ball
from field import Field
from paddle import Paddle
from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
import time

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor('black')
    screen.title('Ping *** Pong Mother***')
    screen.tracer(0)

    paddle_r = Paddle((350, 0))
    paddle_l = Paddle((-350, 0))
    ball = Ball()
    score = Scoreboard()

    screen.listen()
    screen.onkey(key='Up', fun=paddle_r.go_up)
    screen.onkey(key='Down', fun=paddle_r.go_down)
    screen.onkey(key='w', fun=paddle_l.go_up)
    screen.onkey(key='s', fun=paddle_l.go_down)
    # screen.onkey(key='b', fun=ball.move)
    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        ball.move()
        
        # with wall
        if ball.ycor() > 275 or ball.ycor() < -275:
            ball.bounce_y()
        
        # with r_padle
        right_condition = ball.distance(paddle_r) < 50 and ball.xcor() > 320
        left_condition = ball.distance(paddle_l) < 50 and ball.xcor() < -320
        if right_condition or left_condition:
            ball.bounce_x()

        # right
        if ball.xcor() > 380:
            ball.reset_postion()
            score.update_score_right()
        # left
        if ball.xcor() < -380:
            ball.reset_postion()
            score.update_score_left()

        screen.update()
        if score.score_counter_left > 3 or score.score_counter_right > 3:
            game_is_on = False
            score.game_over()

    screen.exitonclick()