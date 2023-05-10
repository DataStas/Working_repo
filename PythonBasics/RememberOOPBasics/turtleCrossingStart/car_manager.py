from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('square')
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.y_start = random.randint(-250, 260)
        self.x_start = random.randint(-250, 260)
        self.goto(self.x_start , self.y_start)
        self.speed = STARTING_MOVE_DISTANCE

    def move(self):
        x_cord = self.xcor() + self.speed
        self.goto(x_cord, self.ycor())

    def reset_position(self):
        self.goto(-270, self.y_start)

    def level_up(self):
        self.speed += MOVE_INCREMENT