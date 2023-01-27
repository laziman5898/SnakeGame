from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Highscore.txt" , mode="r") as file:
            highscore = file.read()
            self.highscore=int(highscore)
        self.penup()
        self.goto(0,300)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} | Highscore : {self.highscore}", align="center", font=("Arial", 24, "normal"))


    def score_up(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score> self.highscore:
            with open("Highscore.txt" , mode="w") as file:
                file.write(f"{self.score}")
            with open("Highscore.txt", mode="r") as file:
                self.highscore = int(file.read())
        self.score=0
        self.update_scoreboard()

