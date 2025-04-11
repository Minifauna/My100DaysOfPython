from turtle import Turtle
from random import choice

POSITIONS = [(-40, 260), (40, 260)]
FONT = ('Arial', 20, 'bold')
COLORS = ['red', 'green', 'blue', 'violet', 'orange', 'indigo', 'white', 'hotpink', 'teal']

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score_keepers = []
        self.create_scoreboards()
        self.midline = Turtle()
        self.midline.rt(90)
        self.draw_midline()
        self.player_score = 0
        self.cpu_score = 0
        self.player_scoreboard = self.score_keepers[0]
        self.cpu_scoreboard = self.score_keepers[1]
        self.player_scoreboard.write(f'{self.player_score}', False, 'center', FONT)
        self.cpu_scoreboard.write(f'{self.cpu_score}', False, 'center', FONT)


    def create_scoreboards(self):
        for position in POSITIONS:
            score_keeper = Turtle()
            score_keeper.pu()
            score_keeper.hideturtle()
            score_keeper.color('white')
            score_keeper.teleport(*position)
            self.score_keepers.append(score_keeper)


    def update_player_score(self):
        self.player_scoreboard.clear()
        self.player_score += 1
        self.player_scoreboard.write(f'{self.player_score}', False, 'center', FONT)

    def update_cpu_score(self):
        self.cpu_scoreboard.clear()
        self.cpu_score += 1
        self.cpu_scoreboard.write(f'{self.cpu_score}', False, 'center', FONT)

    def draw_midline(self):
        self.midline.hideturtle()
        self.midline.pencolor(choice(COLORS))
        self.midline.pensize(3)
        self.midline.teleport(0, 295)
        for x in range(16):
            self.midline.pd()
            self.midline.fd(20)
            self.midline.pu()
            self.midline.fd(20)
            self.midline.pencolor(choice(COLORS))
        self.hideturtle()

    def refresh_midline(self):
        self.midline.clear()
        self.draw_midline()