from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 22, 'normal')


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score_counter_left = 0
        self.score_counter_right = 0
        self.color('White')
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score_counter_left} : {self.score_counter_right}',
                   False, align=ALIGNMENT,
                   font=FONT)       

    def update_score_left(self):
        self.score_counter_left += 1
        self.clear()
        self.update_scoreboard()

    def update_score_right(self):
        self.score_counter_right += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
