from turtle import Turtle
class ball_(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
    def move(self, new_x, new_y):
        self.goto(new_x, new_y)
