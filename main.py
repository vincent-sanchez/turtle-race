from turtle import Turtle,Screen
import random

# Set up screen.
screen = Screen()
screen.setup(width=500,height=400)
screen.title("Turtle Racing")
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")

# Create lists and variables.
colors = ["red","orange","yellow","green","blue","purple","grey","gold"]
turtles = []
y_position = 160
is_race_on = False

# Loop through colors list, create a Turtle object for each color and then line up the turtle against the y-axis.
for color in colors:
    color_type = color
    color = Turtle(shape="turtle")
    color.color(color_type)
    color.penup()
    turtles.append(color)
    y_move = 380/len(colors)
    color.goto(x=-230,y=y_position)
    y_position -= y_move

# If the user has placed a bet, play the game.
if user_bet:
    is_race_on = True
# Play game
while is_race_on:
    for turtle in turtles:
        # If the turtle has passed the x coordinate 230, stop the game and announce winner.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
        # Move the turtle a random number of steps between 0 and 10.
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
# Exit program
screen.exitonclick()
