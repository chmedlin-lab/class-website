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
    else:
        card_text.config(text=flashcards[current_card][1])
        showing_answer = True

def next_card():
    global current_card, showing_answer
    current_card = (current_card + 1) % len(flashcards)
    card_text.config(text=flashcards[current_card][0])
    showing_answer = False


# Window setup
root = tk.Tk()
root.title("Flashcards")
root.geometry("400x300")

# UI elements
card_text = tk.Label(root, text = flashcards[current_card][0], font = ("Arial", 18), wraplength = 350)
card_text.pack(pady=40)

# AI told me to use a comma instead of a period after "Flip". Silly mistake!
flip_button = tk.Button(root, text="Flip", command = flip_card)
flip_button.pack()

next_button = tk.Button(root, text = "Flip", command = flip_card)
next_button.pack(pady=10)


# Run program
root.mainloop()


