import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States Game')
image = "D:\\Pyhton_Dir\\Projects\\Working_repo\\SomeDataEx\\StatesGame\\us-states-game-start\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coor(x:int, y:int) -> None:
    print(x, y)


data = pd.read_csv("D:\\Pyhton_Dir\\Projects\\Working_repo\\SomeDataEx\\StatesGame\\us-states-game-start\\50_states.csv")
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the next State", prompt="What's another state's name?")
    answer_state = answer_state.lower() 
    # answer_state = answer_state.title() 
    states = data['state'].apply(lambda x: x.lower()).to_list()

    if answer_state in states:
        guessed_states.append(answer_state)
        sign = turtle.Turtle()
        sign.hideturtle()
        sign.penup()
        state_data = data[data['state'].apply(lambda x: x.lower()) == answer_state]
        sign.goto(int(state_data.x), int(state_data.y))
        sign.write(f'{str(state_data.state.item())}')

screen.exitonclick()