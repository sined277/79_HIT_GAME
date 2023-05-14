from turtle import Turtle


class Ball(Turtle):

    """Initialize the Ball object with given coordinates"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=1)
        self.shape('circle')
        self.color('white')
        self.x_move = 2  # set horizontal movement speed
        self.y_move = 2  # set vertical movement speed

    def move(self):
        """Method to move the ball"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Method to make the ball bounce vertically"""
        self.y_move *= -1

    def bounce_x(self):
        """Method to make the ball bounce horizontally"""
        self.x_move *= -1

    def reset_ball(self):
        """Method to reset the ball position and horizontal movement"""
        self.goto(0, 0)
        self.bounce_x()
