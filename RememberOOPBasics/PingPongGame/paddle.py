from turtle import Turtle
PADDLE_SIZE = (5, 1)
MOVEMENT_SPEED = 10


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=PADDLE_SIZE[1],
                       stretch_wid=PADDLE_SIZE[0])
        self.penup()
        self.goto(*position)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)