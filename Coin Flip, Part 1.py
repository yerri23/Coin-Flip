
# Program is to generate a random selection of a coin flip,
# heads or tails, using a function from the random package


import random

random.seed()


# Input/initialization

# The variable named 'coin' would be here
# Assign a list with two strings that represent a coin 


coin = ['heads', 'tails']


# Process input into output

# The variable named 'side' representing the side of a coin would be here
# The random choice function will randomly select an item from the list above


side = random.choice(coin)


# Output

# Print out results using the format() method in the print statement
# The purpose is to return a specified value inside the string's placeholder


print('The coin came up {}!'.format(side))

