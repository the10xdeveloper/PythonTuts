#!/usr/bin/env python
# coding: utf-8


'''
This python program calculates the LCM of any two given number
'''
# Request user input for the first number.
numA = input('Enter the first number: ')
# Conver to an integer
numA = int(numA)

# Request user input for the second number.
numB = input('Enter the second number: ')
# Convert to an integer
numB = int(numB)

# Setting an iterator
numI = 1
while numI <= 99999999: # Initializing a while loop
    numI += 1
    if numI % numA == 0 and numI % numB == 0: # Checking if the iterator divides both numbers
        print("The LCM of the numbers", numA, "and", numB, "provided is: ", numI) # Printing the results
        break # Breaks the loop





