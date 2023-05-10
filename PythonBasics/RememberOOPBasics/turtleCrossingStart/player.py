from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.right(-90)
        self.penup()
        self.goto(*STARTING_POSITION)
        self.speed = MOVE_DISTANCE

    def go_up(self):
        new_y = self.ycor() + self.speed
        self.goto(self.xcor(), new_y)

    def go_left(self):
        new_x = self.xcor() - self.speed
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + self.speed
        self.goto(new_x, self.ycor())

    def go_down(self):
        new_y = self.ycor() - self.speed
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto(*STARTING_POSITION)
        self.speed *= 1.5