from turtle import Turtle
class lines_(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=0.4)
    def position(self, position):
        self.goto(position)
