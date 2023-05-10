import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
score = Scoreboard()

screen.onkey(key='Up', fun=player.go_up)
screen.onkey(key='Left', fun=player.go_left)
screen.onkey(key='Right', fun=player.go_right)
screen.onkey(key='Down', fun=player.go_down)

""" можно было всё это запихать в класс и удалять по координате,
 а вместо этого генерировать новое """
cars = []
for _ in range(30):
    cars.append(CarManager())

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    
    for car in cars:
        car.move()
        if car.xcor() > 280 or car.xcor() < -280:
            car.reset_position()

        if car.distance(player) < 26:
            score.game_over()
            game_is_on = False

    if player.xcor() > 275 or player.xcor() < -275:
        score.game_over()
        game_is_on = False

    if player.ycor() > 260:
        for car in cars:
            car.level_up()
        player.reset_position()




    screen.update()

screen.exitonclick()