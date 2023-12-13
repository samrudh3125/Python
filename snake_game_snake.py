from turtle import Turtle,Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:

    def __init__(self):
        self.segments = []
        self.create()
        self.head=self.segments[0]


    def create(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def add_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        self.tail=self.segments[len(self.segments)-1]
        new_segment.goto(self.tail.xcor(),self.tail.ycor())
        self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x,y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(180)
