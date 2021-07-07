from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

condition = True
while condition:
    screen.update()
    time.sleep(0.1)
    snake.move()
#    collision of snake and food
    if snake.head.distance(food) <= 15:
        food.refresh()
        snake.snake_increase()
        score.score_increase()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        condition = False
        score.error_msg()
    for segment in snake.snake_list[3:]:
        if snake.head.distance(segment) < 10:
            condition = False
            score.error_msg()

screen.exitonclick()