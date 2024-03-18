from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.write_score()
    

    def write_score(self):
        self.goto(0,230)
        self.write(f"Score: {self.score}")


    def write_win(self):
        pass


    def add_to_score(self):
        self.score += 1