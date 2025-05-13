from turtle import Turtle
import os 

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        if not os.path.exists("data.txt"):
            with open("data.txt", mode="w") as data:
                data.write("0")
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over.", align="center", font=("Arial", 24, "normal"))
    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Arial", 24, "normal"))

    def reset_scoreboard(self):
        if self.highscore < self.score:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()
