from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-225, 260)
        self.write(f"level = {self.level}", align="center", font=FONT)

    def point(self):
        self.level += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.clear()
        self.update_scoreboard()
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
