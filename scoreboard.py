# IMPORT
from turtle import Turtle

# VARIABLES
ALIGNMENT = 'center'
FONT = ('Arial', 12, 'normal')

# CLASS
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.teleport(0, 270)
        self.write_score()
        self.hideturtle()

    def clear_score(self):
        self.clear()

    def write_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1

    def game_over(self):
        self.teleport(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
