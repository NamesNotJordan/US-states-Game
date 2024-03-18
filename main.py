import pandas
import turtle
from state_writer import StateWriter
from scoreboard import ScoreBoard

#Build screen
screen = turtle.Screen()
screen.title("Name the States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


state_writer = StateWriter()
scoreboard = ScoreBoard()
correct_answers = []
# Pandas stuff
data = pandas.read_csv("50_states.csv")


game_on = True
while game_on:
    answer_state = screen.textinput(title="Name a State", prompt="Take a guess").title()
    scoreboard.add_to_guesses()

    if answer_state in data["state"].array:
        correct_answers.append(answer_state)
        scoreboard.add_to_score()
        state_data = data[data["state"] == answer_state]
        state_writer.write_state(answer_state,int(state_data["x"]),int(state_data["y"]))
    
    scoreboard.update_score()
    
    if scoreboard.has_guessed_all_states():
        state_writer.write_win()

turtle.mainloop