from turtle import Turtle
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-220, 250)
        self.writer()

    def inc(self):
        self.score += 1
        self.clear()
        self.writer()

    def writer(self):
        self.write(f"Level : {self.score}", False, "center", FONT)

