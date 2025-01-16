# IMPORTS
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Score
import time

# SCREEN SETUP
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.colormode(255)
screen.tracer(0) # turning off animation

# VARIABLES
game_is_on = True

# CREATING A SNAKE BODY AND FOOD AND SCORE
snake = Snake()
food = Food()
score = Score()

# LISTENING FOR KEYPRESS
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# GAME LOGIC
while game_is_on:
    screen.update() # calling to update screen
    time.sleep(0.1) # delay by 0.1 sec

    snake.move() # move snake

    # Detect collision with food
    if snake.head.distance(food) < 15:
        score.clear_score() # clear scoreboard
        score.update_score() # add 1 point
        score.write_score() # display score again
        food.refresh()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < - 280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]: # loop through the snake segments other than the first one
        # if head collides with any segment in the tail: trigger game_over
        if snake.head.distance(segment) < 10:
            game_is_on: False
            score.game_over()

# EXIT ON CLICK
screen.exitonclick()