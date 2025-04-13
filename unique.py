"""
Author: Cristian Alvarez
Date: 4/13/2025
Program: Module 4 Exercise 5-7
Version: 1.0
"""

# Ask user for the file name
fileName = input("Enter the input file name: ")

try:
    # Opening the file so that the program can read it
    inputFile = open(fileName, 'r')

    # Create an empty list to store words that we seen for the first time
    wordsSeen = []

    # iterates through each line of the file
    for line in inputFile:
        words = line.split()

        for word in words:
            # take away punctuation
            word = word.strip('.,!?";:-()')

            # Add word if not already in the list
            if word not in wordsSeen:
                wordsSeen.append(word)

    # Close the file
    inputFile.close()

    # sort the list
    wordsSeen.sort()

    # output each word
    for word in wordsSeen:
        print(word)

except FileNotFoundError:
    print(f"File '{fileName}' not found.")