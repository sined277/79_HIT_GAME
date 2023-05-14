from turtle import *
import random

# List of possible colors for bricks
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class BrickManager:
    def __init__(self):
        # List to hold all the brick turtles
        self.brick_lists = []

        # Starting x position for first brick
        x = -380

        # Loop to create all the bricks
        while x < 380:
            # Create four rows of bricks at each x position
            self.create_brick(x, 150)
            self.create_brick(x, 175)
            self.create_brick(x, 200)
            self.create_brick(x, 225)
            # Increase x position for next set of bricks
            x += 42

    def create_brick(self, xpos, ypos):
        # Create a new Turtle object to represent the brick
        t = Turtle()

        # Set the turtle's shape, penup, and size attributes
        t.shape("square")
        t.penup()
        t.shapesize(stretch_len=2)

        # Set the turtle's color randomly from the list of colors
        t.color(random.choice(COLORS))

        # Point the turtle upwards and move it to the correct position
        t.left(180)
        t.goto(xpos, ypos)

        # Add the new brick turtle to the list of bricks
        self.brick_lists.append(t)

    def remove(self, brick):
        # Remove a given brick turtle from the list of bricks
        self.brick_lists.remove(brick)
