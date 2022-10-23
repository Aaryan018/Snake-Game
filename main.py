from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

#it means the screen will not update (animation won't play on screen) unless screen.update() is used.
screen.tracer(0)

#activates the screen to start listening to various events
screen.listen()

snake = Snake()
food = Food()
score = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on = True

#Moving the snake
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.change_location()
        score.update_score()
        snake.extend()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_score()
        snake.reset_snake()

    #detect collision with the tail
    #the snake.segments list is sliced so that the snake.head is not compared to itself.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()



screen.exitonclick()