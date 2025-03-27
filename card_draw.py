# Python program to simulate drawing cards from a shuffled deck

# Importing necessary modules
import itertools
import random

# Create a deck of cards with values 1 to 13 and suits Spade, Heart, Diamond, Club
deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))

# Shuffle the deck of cards
random.shuffle(deck)

# Draw and display five cards from the shuffled deck
if len(deck) >= 5:
    print("You got:")
    for i in range(5):
        print(deck[i][0], "of", deck[i][1])
else:
    print("Not enough cards in the deck to draw five cards.")
