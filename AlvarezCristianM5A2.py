"""
Author: Cristian Alvarez
Assignment: Module 5 Assignment 1
Date: 4/21/2025
Verison: 1.0
"""

import random #importing the random module so we can access the random integer function

def randomNum():
    answer = random.randint(1,100) #using the random function so the program can guess a random number. using the answer variable to store it
    guessOne = int(input("Guess a number between 1 - 100: ")) #asking the user to make their first guess

    while guessOne != answer: #while loop since we dont know how many tries its going to take the user
        if guessOne > answer:
            print("Too high. Try again.") #output if guess is too high
        elif guessOne < answer:
            print("Too low. Try again.") #output is guess is too low

        guessOne = int(input("Guess a number between 1 - 100: ")) #asking the priming statement again

    print(f"You guessed {guessOne} and the correct answer was {answer}. You guessed correctly!") #output if you guess correctly


def playMore(): #creating a new function that includes the randomNum() function is a while loop. this is so the user can play as many times as they want. or they can just play once
    while True:
        randomNum()
        oneMoreGame = input("Would you like to one more time? (y or n): ").lower()
        if oneMoreGame != "y": #if user types in anything but y then they will not play again.
            print("Thank you for playing. Please come back!")
            break

playMore()