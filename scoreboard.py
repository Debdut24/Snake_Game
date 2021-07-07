from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 260)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score_display()

    def score_increase(self):
        self.clear()
        self.score += 1
        self.score_display()

    def score_display(self):
        # self.write("Lvl 1", move=False, align="center", font=("Arial", 18, "normal"))
        self.write(f"\nScore : {self.score}", move=False, align="center", font=("Arial", 18, "normal"))

    def error_msg(self):
        error = Turtle()
        error.color("white")
        error.hideturtle()
        error.write(f"Game Over !", move=False, align="center", font=("Arial", 28, "normal"))