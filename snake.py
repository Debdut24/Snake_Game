import turtle
from turtle import Turtle
class Snake:
    def __init__(self):
        coordinates = [(0, 0), (20, 0), (40, 0)]
        self.snake_list = []
        for c in coordinates:
            new_turtle = Turtle("circle")
            new_turtle.goto(c)
            new_turtle.color("white")
            new_turtle.penup()
            self.snake_list.append(new_turtle)
        self.head = self.snake_list[0]

    def snake_increase(self):
        self.snake_append(self.snake_list[-1].position())

    def snake_append(self, position):
        new_turtle = Turtle("circle")
        new_turtle.goto(position)
        new_turtle.color("white")
        new_turtle.penup()
        self.snake_list.append(new_turtle)

    def move(self):
        length = len(self.snake_list)
        for n in range(length - 1, 0, -1):
            x = self.snake_list[n - 1].xcor()
            y = self.snake_list[n - 1].ycor()
            self.snake_list[n].goto(x, y)
        self.snake_list[0].forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
