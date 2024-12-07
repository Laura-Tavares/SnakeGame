### Setting up
import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Score

### Screen aesthetic
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("lavender")
screen.title("Laura's Snake Game!")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Score()

### Control the snake with keypress
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    x = snake.head.xcor()
    y = snake.head.ycor()
    if x > 290 or x < -290 or y > 290 or y < -290:
        scoreboard.reset()
        snake.reset()
        # game_is_on = False
        # scoreboard.game_over()

    # Detect collision with tail
    for square in snake.snake:
        if square == snake.head:
            pass
        elif snake.head.distance(square) <10:
            scoreboard.reset()
            snake.reset()
            # game_is_on = False
            # scoreboard.game_over()


screen.exitonclick()