"""
Author: Cristian Alvarez
Date: 4/13/25
Assignment: M4 Practice Exercise 5-8
Version: 1.0
"""

inName = input("Please enter the name of the file: ") #asking for file name

inputFile = open(inName, "r") #reading the file

uniqueWords = {} #creating a dictionary to store the word and their frequencies

for line in inputFile: #iterating through the file
    words = line.split() #turning each line into their own list

    for word in words: #iterating through words to get each word on its own
        word = word.strip(',".?!;:-()') #cleaning the word so nothing else besides the word gets outputted

        if word in uniqueWords: #checking if the word is in our dictionary
            uniqueWords[word] += 1 #if it is then we increase the value by 1
        else:
            uniqueWords[word] = 1 #if its not then we add it to our dictionary

inputFile.close() #closing the file

wordList = list(uniqueWords.keys()) # turning our dictionary in to a list
wordList.sort() #sorting our new list

for word in wordList:
    print(word, uniqueWords[word]) #printing the word and its value



