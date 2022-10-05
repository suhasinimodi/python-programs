from turtle import Turtle, color

class Scoreboard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.current_score = 0
        self.goto(position)
        self.color("white")
        self.write(f"Score: {self.current_score}", align="center", font=("Arial",22,"normal"))   
        self.hideturtle() 

    def increase_score(self):
        self.current_score += 1
        self.clear()
        self.write(f"Score: {self.current_score}", align="center", font=("Arial",22,"normal")) 
        