from turtle import Turtle
MOVE_DISTANCE = 20
COORDINATE_CHANGE = 20
class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()


    def create_snake(self):
        xcor = 0
        for turtle in range(3):
            timmy = Turtle(shape="square")
            timmy.color("white")
            timmy.penup()
            timmy.goto(xcor, 0)
            xcor -= COORDINATE_CHANGE
            self.turtles.append(timmy)

    def tail(self):
        last_segment = self.turtles[-1]
        last_xcor = last_segment.xcor()
        last_ycor = last_segment.ycor()

        timmy = Turtle(shape="square")
        timmy.color("white")
        timmy.penup()
        timmy.goto(last_xcor, last_ycor)
        self.turtles.append(timmy)


    '''How does the below code work? / How does the snake make its movement?
    Answer: Here, we are using a while loop to set up the continuous movement of the 
    snake, unless the condition turns false. 
    screen.update() is allowing us to update the screen only after all the three segments
    of the snake a=have moved altogether and time.sleep() helps us to control the speed of the
    snake. 
    The for loop, uses a range function to loop through each segment of the snake, 
    It starts from the last segment and updates the x and y coordinates of that segment and \
    changes it to the coordinates of the preceding segment.
    why? - because if the snake needs to make a turn, we want the body to follow the
    head and not keep goinf forward on its own.'''


    def move(self):
        for turtle_num in range(len(self.turtles)-1, 0, -1):
            x = self.turtles[turtle_num-1].xcor()
            y = self.turtles[turtle_num-1].ycor()
            self.turtles[turtle_num].goto(x, y)
        self.turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].setheading(90)

    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)

    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)

    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)

