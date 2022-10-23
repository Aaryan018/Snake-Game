from turtle import Turtle


class Snake:

    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for positions in self.starting_positions:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.setpos(positions)
            self.segments.append(new_segment)


    def reset_snake(self):
        for segment in self.segments:
            segment.setpos(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


#adds a new segment to the snake and increase its length
    def extend(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(self.segments[-1].position())
        self.segments.append(new_segment)


    # The segment at index i takes the position of segment at index i-1. This way the tail of the
    # snake will always follow its head
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].setpos(x, y)

        self.segments[0].forward(20)




    #makes the head go in up direction
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    #makes the head go in down direction
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    #makes the head go in left direction
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    #makes the head go in right direction
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
