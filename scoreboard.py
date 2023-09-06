from turtle import Turtle

ALIGNEMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.speed("fastest")
        self.hideturtle()
        self.refresh_score()

    def refresh_score(self):
        self.write(f"Score: {self.score} ", False, align=ALIGNEMENT, font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER ", False, align=ALIGNEMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh_score()
