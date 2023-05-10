import turtle as t
import random


def random_color():
    return (random.randint(0, 255), random.randint(0, 255),
            random.randint(0, 255))


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 10)


tim = t.Turtle()
t.colormode(255)
tim.speed('fastest') 
draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()