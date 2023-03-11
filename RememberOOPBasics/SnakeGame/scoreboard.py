from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 22, 'normal')


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score_counter = 0
        self.color('Green')
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: = {self.score_counter}',
                   False, align=ALIGNMENT,
                   font=FONT)       

    def update_score(self):
        self.score_counter += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
