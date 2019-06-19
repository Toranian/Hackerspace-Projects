import random
from die import Die
from bag_of_dice import BagOfDice

# Creates a bag of three, six-sided die.
bag_of_die = [ Die(6) for i in range(3)]
bag = BagOfDice(bag_of_die)
print(bag.roll()) # Rolls and prints the TOTAL of all the rolls in the bag.