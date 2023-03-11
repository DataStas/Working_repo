import turtle as t
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_c = (r, g, b)
    return random_c


tim = t.Turtle()
tim.screen.colormode(255)
tim.width(10)
tim.screen.setup(width=500, height=500, startx=500, starty=500)

colours = ['CornflowerBlue',
           'DarkOrchid',
           'IndianRed',
           'DeepSkyBlue',
           'LightSeaGreen',
           'wheat',
           'SlateGray', 
           'SeaGreen']
dircetions = [0, 90, 180, 270]

for _ in range(200):
    # tim.color(random.choice(colours))
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(dircetions))