"""
Author: Cristian Alvarez
Date: 4/27/2025
Program: Module 6 Assignment
Version: 1.0
"""

import tkinter as tk

window = tk.Tk() #creating the window
window.geometry("400x300") #size of the window

label = tk.Label(text="Temperature Conversion Program", #creating our label
                 font=("Arial", 20, "bold"))
label.pack(pady=20)

tempEntry = tk.Entry(window) #creating the entry box so the user can enter a temp
tempEntry.pack(pady=10)


def convertToFarenheit(): #our function to convert celsius to fahrenheit
    celsius = tempEntry.get() #gets the information that was enter in the box
    celsius = float(celsius) #converts input to float
    farenheit = (9/5) * celsius + 32 #formula
    #print(farenheit)
    resultLabel.config(text=f"{farenheit:.2f} deg F") #alters our result label to print the answer

def convertToCelsius(): #pretty much same thing as the fahrenheit function but with celsius
    farenheit = tempEntry.get()
    farenheit = float(farenheit)
    celsius = (5/9) * (farenheit - 32)
    resultLabel.config(text=f"{celsius:.2f} deg C")

button = tk.Button(text="Convert to Fahrenheit", command=convertToFarenheit) #button to call the convert to fahrenheit function
button.pack(pady=5)

ftoCButton = tk.Button(text="Convert to Celsius", command=convertToCelsius) #button to call the convert to celsius function
ftoCButton.pack(pady=5)

resultLabel = tk.Label(window, text="") #label to print the result
resultLabel.pack(pady=5)

window.mainloop()
