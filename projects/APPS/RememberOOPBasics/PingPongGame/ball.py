from turtle import Turtle
INITIAL_POSITION = (0, 0)
MOVEMENT_SPEED = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_len=1,
                       stretch_wid=1)
        self.penup()
        self.goto(*INITIAL_POSITION)
        self.x_move = MOVEMENT_SPEED
        self.y_move = MOVEMENT_SPEED
        self.move_speed = 0.1

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move = -self.y_move
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move = -self.x_move
        self.move_speed *= 0.9
    
    def reset_postion(self):
        self.goto(0, 0)
        self.bounce_x()