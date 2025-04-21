"""
Author: Cristian Alvarez
Date: 4/20/2025
Program: Module 5 Exercise 7-5
Version: 1.0
"""
def printAll(seq): #defines the function
    if seq:
        print(seq, "->", seq[0])  #going to print the full list the first time we call
        printAll(seq[1:]) #going to output everything except the first item

testList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #sample list to make sure it works

print("Testing printAll with:", testList) #outputting out information. letting user know what we are doing

printAll(testList) #outputs the results