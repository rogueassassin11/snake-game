# IMPORTS
from turtle import Turtle

# VARIABLES
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# CONSTRUCTORS
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_body = Turtle()
        snake_body.penup()
        snake_body.shape("square")
        snake_body.color("white")
        snake_body.goto(position)
        self.segments.append(snake_body)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # MOVING THE SNAKE BODY
        for seg_num in range(len(self.segments) - 1, 0, -1):  # start=len(snake), stop=0, step=-1
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)