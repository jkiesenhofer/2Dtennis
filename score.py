from turtle import Turtle
class score_(Turtle):
    def __init__(self):
        super().__init__()
        self.color('cyan')
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
    def rsup(self):
        self.r_score += 1
        self.update_score()
    def lsup(self):
        self.l_score += 1
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal'))
