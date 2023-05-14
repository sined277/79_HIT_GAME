from turtle import Turtle

# Set constants for paddle direction
UP = 90
DOWN = 270


class Paddle(Turtle):

    # Initialize the Paddle object with given coordinates
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.setheading(90)     # set the heading of turtle to upwards
        self.penup()            # don't draw lines while moving the turtle
        self.goto(x_cor, y_cor)  # set the paddle at given coordinates
        self.turtlesize(15, 1)  # set the size of paddle
        self.shape('square')
        self.color('white')

    # Move the paddle to the right
    def move_right(self):
        new_x = self.xcor() + 80
        self.goto(new_x, self.ycor())

    # Move the paddle to the left
    def move_left(self):
        new_x = self.xcor() - 80
        self.goto(new_x, self.ycor())
