from turtle import Turtle

ALIGNMENT ="center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.total_guesses = 0
        self.penup()
        self.hideturtle()
        self.write_score()
    

    def write_score(self):
        self.goto(0,230)
        self.write(f"Score: {self.score}/{self.total_guesses}")


    def update_score(self):
        self.clear()
        self.write_score()

    def write_win(self):
        self.goto(0,0)
        self.write(f"You named all 50 states! It only took {self.total_guesses} tries :)", align=ALIGNMENT)


    def add_to_score(self):
        self.score += 1


    def add_to_guesses(self):
        self.total_guesses += 1

    def has_guessed_all_states(self):
        return self.score == 50