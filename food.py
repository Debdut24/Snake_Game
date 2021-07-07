from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.penup()
        self.goto(x, y)
        self.speed("fastest")

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)