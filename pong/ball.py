from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.xmov = 10
        self.ymov = 10
        self.move_speed = 0.1

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("slowest")

    def move(self):
        x = self.xcor() + self.xmov
        y = self.ycor() + self.ymov
        self.goto(x,y)

    def bounce_y(self):
        self.ymov *= -1

    def bounce_x(self):
        self.xmov *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1