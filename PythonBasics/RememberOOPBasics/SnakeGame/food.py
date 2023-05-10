from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        # from superclass
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('white')
        self.speed('fastest')
        self.new_random_location()

    def new_random_location(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)