from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial',14,'normal')
G_O_FONT = ('Arial', 48, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.sety(280)
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.write(f'Score: {self.score}', False, ALIGNMENT,FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', False, ALIGNMENT,FONT)

    def game_over(self):
        self.teleport(0,0)
        self.color('crimson')
        self.write('YOU DIED...', False, ALIGNMENT, G_O_FONT)
