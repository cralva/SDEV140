"""
Author: Cristian Alvarez
Date: 4/20/2025
Program: Module 5 Exercise 6-6
Version: 1.0
"""

def myRange(start, stop=None, step=1): #this is where we start our range function
    result = []  #initializing our list

    if stop is None: #if one argument is given then it is the stop value
        stop = start
        start = 0

    if step == 0: #step cant be zero since we are creating a range. we need to go up or down
        print("Step can't be zero!")
        return []

    if step > 0: #if statement so we can count up
        while start < stop:
            result.append(start)
            start = start + step

    else: #statement to count down
        while start > stop:
            result.append(start)
            start = start + step

    return result

print(myRange(10))
print(myRange(1, 10))
print(myRange(1, 10, 2))