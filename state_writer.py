from turtle import Turtle

FONT = ()
ALIGNMENT = "center"

class StateWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        

    def write_state(self, state_name, x, y):
        self.goto(x, y)
        self.write(state_name, align=ALIGNMENT)
    
    
    def write_win(self):
        self.goto(0,0)
        self.write("You named all 50 states!", align=ALIGNMENT)