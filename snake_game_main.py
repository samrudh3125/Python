from snake import Snake
from food import Food
from turtle import Screen
from scoreboard import Scoreboard
import time

scoreboard = Scoreboard(0)

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game by Samrudh")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecting when the snake eats the food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.add_segment()
        food.set_position()

    # Detecting when the snake touches the wall
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detecting if the snake touches its own body
    for segment in snake.segments[2:]:
        if snake.head.distance(segment) <= 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
