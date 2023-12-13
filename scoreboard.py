from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, score):
        super().__init__()
        self.score=score
        self.color("white")
        self.shapesize(0.00001,0.00001)
        self.penup()
        self.goto(0,250)
        self.display()

    def display(self):
        self.write(f"Score: {self.score}", False, "center", ("Arial", 15, "normal"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.display()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",False,"center",("Arial",20,"normal"))