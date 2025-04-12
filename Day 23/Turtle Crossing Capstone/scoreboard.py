from turtle import Turtle

FONT = ("Courier", 24, "normal")
G_O_FONT = ("Courier", 40, "normal")
SCORE_POS = (-275, 250)


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.level = 0
        self.score_keeper = Turtle()
        self.score_keeper.hideturtle()
        self.score_keeper.pu()
        self.score_keeper.teleport(*SCORE_POS)
        self.score_keeper.color('white')
        self.score_keeper.write(f'Level: {self.level}', False, 'left', FONT)


    def update_level(self):
        self.score_keeper.clear()
        self.level += 1
        self.score_keeper.write(f'Level: {self.level}', False, 'left', FONT)

    def game_over(self):
        self.score_keeper.teleport(0,0)
        self.score_keeper.color('crimson')
        self.score_keeper.write('GAME OVER', False, 'center', G_O_FONT)
        return False