#!/usr/bin/env python
# coding: utf-8

# In[9]:


""" This python program checks and finds the perfect square of any given number.
"""

# Prompt the user to enter a given number.
print("Enter a number to see if it\'s a perfect square.")
# Setup a variable to request for user input.
userInput = input('Please enter a number: ')
# Ensure the number is a positive integer
userInput = abs(int(userInput))
# Setting up an iterator variable
i = -1
# Initializing a boolean to check for perfect square
square = False
# Initialize a while loop from -1 to the square root of the number
while i <= userInput**(0.5):
    # Increase i by 1
    i += 1
    # Checking the square root of the number
    if i*i == userInput:
        square = True
        break
if square:
    print('The square root of ', userInput, 'is', i, '.')
else:
    print('', userInput, ' is not a perfect square.')


# In[ ]:




