# IMPORTS
from turtle import Screen, Turtle
from snake import Snake
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

# CREATING A SNAKE BODY
snake = Snake()

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

    snake.move()


# EXIT ON CLICK
screen.exitonclick()