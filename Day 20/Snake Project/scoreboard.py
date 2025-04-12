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
        self.high_score = int((open('data.txt').read()))
        open('data.txt').close()
        self.write(f'Score: {self.score} High Score: {self.high_score}', False, ALIGNMENT,FONT)

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', False, ALIGNMENT,FONT)

    def increase_score(self):
        self.score += 1


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()


    # def game_over(self):
    #     self.teleport(0,0)
    #     self.color('crimson')
    #     self.write('YOU DIED...', False, ALIGNMENT, G_O_FONT)
