from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.color("blue")
        self.set_position()

    def set_position(self):
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        self.goto(x,y)
