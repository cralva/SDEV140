"""
Author: Cristian Alvarez
Date: 4/13/25
Assignment: M4 Assignment Part 1
Version: 1.0
"""

#initalization
userInt = 0
numbersList = []

#get data
userInt = int(input("Enter a number greater than 1: ")) #getting the user input

#process data
if userInt <= 1: #if statement to check and make sure that the user response was valid
    print("That is not a valid response!")

numbersList = list(range(2, userInt + 1)) #creating our list

def is_prime(number): #defining our function to check and see what the prime numbers are
    for i in range(2, number): #to iterate through each number
        if number % i == 0: #checks if it is a prime number. if equals to 0 then it is not a prime number
            return False
    return True

for number in numbersList: #iterates through the number list
    if is_prime(number): #checks if its prime.
#output information
        print(f"{number} is a prime number!")

