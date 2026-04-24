import tkinter as tk

# Asked AI to come up with an outline for the coding
# Flashcard data
flashcards = [
    ("Slope intercept form", "y=mx+b"),
    ("Standard form", "Ax+Bx=Cx"),
    ("Point-slope form", "y-y1 = m(x-x1)")
    ("Slope", "A measure of the steepness and direction of a line")
    ("Rate of Change", "A ratio that compares the amount of change in a dependent variable to the amount of change in an independent variable.") 
]

# State variable
current_card = 0
showing_answer = False

# Functions
def flip_card():
    global showing_answer
    if showing_answer:
        card_text.config(text=flashcards[current_card][0])
        showing_answer = False


# Window setup


# UI elements


# Run program


