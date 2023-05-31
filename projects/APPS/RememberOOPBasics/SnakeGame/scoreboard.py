from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 21, 'normal')


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.high_score = 0
        self.read_high_score()
        self.score_counter = 0
        self.color('White')
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: = {self.score_counter} High Score: {self.high_score}',
                   False, align=ALIGNMENT,
                   font=FONT)       

    def read_high_score(self):
        with open('data.txt', mode='r') as file:
            self.high_score = int(file.read())

    def reset(self):
        if self.score_counter > self.high_score:
            self.high_score = self.score_counter
            with open('data.txt', mode='w') as file:
                file.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()

    def update_score(self):
        self.score_counter += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
