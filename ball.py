from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        # self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        # we only modified ycor, xcor is doing its job perfectly by moving on its cors.
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
