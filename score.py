from turtle import Turtle

class Score:

    def __init__(self):
        self.score_text = Turtle()
        self.score_text.penup()
        self.score_text.hideturtle()
        self.score_text.color("green")
        self.score = 0
        self.highscore = 0
        self.score_text.goto(x= 0,y=250)
        self.score_text.write(f"Score: {self.score} | HighScore: {self.highscore}" , font=("Courier", 16,""), align="center")

    def update_score(self):
        self.score += 1
        self.score_text.undo()
        self.score_text.write(f"Score : {self.score} | HighScore: {self.highscore}", font=("Courier", 16, ""), align="center")

    def reset_score(self):
        self.score = 0
        self.score_text.undo()
        self.score_text.write(f"Score : {self.score} | HighScore: {self.highscore}", font=("Courier", 16, ""), align="center")

    def update_high(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", "w") as f:
                f.write(str(self.highscore))


