""" Turtle Event Listiners """
from turtle import Turtle, Screen
import functools


tim = Turtle()
screen = Screen()
global speed, speed_rate
speed = 10
speed_rate = 10

""" My first decorator """


def SpeedIncreaseDecorator(move_forwards):
    @functools.wraps(move_forwards)
    def Increase():
        global speed, speed_rate
        speed = speed + speed_rate
        print(f'I m in decorator, Speed is: {speed}')
        move_forwards(speed)
    return Increase


@SpeedIncreaseDecorator
def move_forwards(speed):
    tim.forward(speed)


def SpeedDecreaseDecorator(move_forwards):
    @functools.wraps(move_forwards)
    def Decrease():
        global speed, speed_rate
        speed = speed - speed_rate
        print(f'I m in decorator, Speed is: {speed}')
        move_forwards(speed)
    return Decrease


@SpeedDecreaseDecorator
def move_backward(speed):
    tim.backward(speed)


def counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading) 


def clear_drowing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def set_speed_rate():
    global speed_rate
    speed_rate = int(screen.textinput(title="Change_speed_bar",
                                      prompt='Input new speed rate'))
    screen.listen()

screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=counter_clockwise)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='c', fun=clear_drowing)
screen.onkey(key='n', fun=set_speed_rate)
screen.exitonclick()
