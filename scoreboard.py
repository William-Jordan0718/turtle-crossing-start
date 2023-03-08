from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEFT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280,250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=LEFT, font=FONT)

    def player_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"KICK ROCKS BUDDY!", align="center", font=FONT)

