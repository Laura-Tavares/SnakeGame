from turtle import Turtle

with open("record_track.txt") as f:
    last_hs = f.read()

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(last_hs)
        self.color("HotPink4")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score = {self.score} Record = {self.high_score}", align="center", font=("Calibri", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("record_track.txt", mode="w") as f:
            f.write(f"{str(self.high_score)}")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    #def game_over(self):
    #    self.goto(0,0)
    #    self.write(arg="GAME OVER", align="center", font=("Courier", 24, "normal"))