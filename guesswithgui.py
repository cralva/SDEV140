"""
Author: Cristian Alvarez
Date: 4/126/2025
Program: Module 6 Exercise 9-5
Version: 1.0
"""

import tkinter as tk #importing tkinter to use GUI

window = tk.Tk() #instantiating my window
window.title("Guessing Game") #title

low = 1
high = 100

def newGame(): #need a function so when new game it pressed that it restarts
    global high, low
    low = 1
    high = 100
    makeGuess()

def makeGuess(): #making an initial function to start the guessing game
    global low, high
    guess = (low + high) // 2
    label.config(text=f"Is it {guess}?")
    window.currentGuess = guess

    buttonSmall.config(state="normal")
    buttonLarge.config(state="normal")
    buttonCorrect.config(state="normal")


def tooSmall(): #a function for the program if the guess it too small
    global low
    low = window.currentGuess + 1
    makeGuess()

def tooLarge(): #function when the guess it too big
    global high
    high = window.currentGuess - 1
    makeGuess()

def correct(): #correct function
    label.config(text=f"I knew it! The correct answer was {window.currentGuess}!")
    buttonSmall.config(state="disabled") #disabling the buttons if the guess is correct
    buttonLarge.config(state="disabled")
    buttonCorrect.config(state="disabled")




label = tk.Label(window, text="Click 'New Game' to start", font=("Arial", 20)) #our first label to start the game
label.pack(pady=20)

buttonSmall = tk.Button(window, text="Too Small", command=tooSmall) #button for the too small hint
buttonSmall.pack(pady=5)

buttonLarge = tk.Button(window, text="Too Large", command=tooLarge)#button for the too big hint
buttonLarge.pack(pady=5)

buttonCorrect = tk.Button(window, text="Correct!", command=correct)#button for the correct hint
buttonCorrect.pack(pady=5)

buttonNew = tk.Button(window, text="New Game", command=newGame) #button to start a new game
buttonNew.pack(pady=20)

window.mainloop()