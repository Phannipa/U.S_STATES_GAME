# from turtle import Turtle, Screen
# turtle = Turtle()
# screen = Screen()
# screen.title("U.S. States Game")
# image = "Blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)
# screen.exitonclick()

import turtle
import pandas

screen = turtle.Screen() # Created screen object from Turtle class.
screen.title("U.S. States Game")
image = "Blank_states_img.gif" # turtle only works with gif format, cannot use png or jpeg.
screen.addshape(image) # Loaded new image as a new shape.
turtle.shape(image)

# Access to dataframe of csv file
data = pandas.read_csv("50_states.csv")
print(data)

# Get series of csv file
state = data["state"]

# Make a list of state
state_list = state.to_list()
print(state_list)


# we will win when we guess all of 50 states. If guess is wrong, just only repeat to get new prompt.
# We have to keep answer in to the list and loop it until it reach to 50 states.
guess_state = []

while len(guess_state) < 50:
    # Make a prompt to ask the user and keep track of the number of states
    answer_state = screen.textinput(title=f"{len(guess_state)}/50 States Correct", prompt="What's another state game")
    guess = answer_state.capitalize() # Or using answer_state.title()
    print(guess)

    # 2.Check if the guess is one of the 50 states. If it's right,
    # create a turtle to writhe the name of the state at the state's x and y coordinate.

    if guess in state_list:
        guess_state.append(guess) # If guess is corrected, add in to the list
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        correct_guess = data[data.state == guess] # Get a row data
        t.goto(x=int(correct_guess.x), y=int(correct_guess.y))  # This is the row of data and we can tap into an attribute using the name of column.
        t.write(guess, font=("Verdana", 15, "normal"))

    # If we want to exit and list of states that we didn't guess them in to new csv file.
    if guess == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guess_state: # It means it's missing, not in the list.
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states) # When we create dataframe, we can use list.
        new_data.to_csv("states_to_learn.csv")
        break


# screen.exitonclick() Skip this code, when we exit the game. So it doesn't show the screen when we exit.

