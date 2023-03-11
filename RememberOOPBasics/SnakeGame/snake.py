from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWNN = 270
RIGHT = 0
LEFT = 180


class Snake(Turtle):
    def __init__(self) -> None:
        self.segments = []
        self.set_snake_start()
        self.head = self.segments[0]

    def set_snake_start(self):
        for position in STARTING_POSITIONS:
            new_segmennt = Turtle('square')
            new_segmennt.color('white')
            new_segmennt.penup()
            new_segmennt.goto(position)
            self.segments.append(new_segmennt)

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def add_segment(self, position):
            new_segmennt = Turtle('square')
            new_segmennt.color('white')
            new_segmennt.penup()
            new_segmennt.goto(position)
            self.segments.append(new_segmennt)
    
    def growth(self):
        # add a new segment to the shake
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWNN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWNN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
