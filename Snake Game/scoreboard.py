from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial',24,'normal')
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,265)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align = ALIGNMENT, font= FONT)
        self.score = 0

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align = ALIGNMENT, font= FONT)