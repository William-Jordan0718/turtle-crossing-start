from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
HEADING = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(HEADING)
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)

    # get turtle to change Y axis.
    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    # when turtle crosses finish
    def reset_position(self):
        self.goto(STARTING_POSITION)

