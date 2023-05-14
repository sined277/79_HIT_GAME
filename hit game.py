from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from brick import BrickManager
import random

# Create the game screen
my_screen = Screen()
my_screen.bgcolor('Black')
my_screen.setup(width=800, height=600)
my_screen.title('HIT GAME')
my_screen.tracer(0)

# Create the paddle, bricks, and ball
paddle = Paddle(0, -250)
brick_manager = BrickManager()
ball = Ball()

# Listen for keyboard inputs to move the paddle
my_screen.listen()
my_screen.onkey(paddle.move_left, 'a')
my_screen.onkey(paddle.move_right, 'd')

# Game loop
game_is_on = True
while game_is_on:
    my_screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 290:
        ball.bounce_y()
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.bounce_x()

    # Detect collision with the bottom wall and reset the ball
    if ball.ycor() < -290:
        ball.reset_ball()

    # Detect collision with the paddle and bounce the ball back
    if ball.distance(paddle) < 150 and abs(ball.ycor() - paddle.ycor()) < 20:
        ball.bounce_y()

    # Detect collision with bricks and remove them
    for brick in brick_manager.brick_lists:
        if ball.distance(brick) < 20:
            brick.goto(500, 0)  # Move the brick off-screen
            brick_manager.remove(brick)  # Remove the brick from the brick manager
            print(len(brick_manager.brick_lists))
            ball.bounce_y()

    # End the game if all bricks are removed
    if len(brick_manager.brick_lists) == 0:
        my_screen.update()
        game_is_on = False

# Close the game window when the game is over
my_screen.exitonclick()
