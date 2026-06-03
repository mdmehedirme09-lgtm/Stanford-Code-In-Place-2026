"""
File: dicesimulator.py
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""

"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!

Note: The starter code for this example is the solution.
"""

# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
NUM_SIDES = 6
NUM_ROLLS=3

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    #total = die1 + die2
    #print("Total of two dice:", total)
    #return die1,die2
    print(f"Die 1 = {die1}")
    print(f"Die 2 = {die2}")
    total=die1+die2
    print(f"Total(Die 1+Die 2) = {die1 + die2}")

def main():
    # Set a seed to help with debugging (you can comment it out to make the results random!)
    random.seed(1)
    
    # die1 = 10
    # die2=0
    # print("die1 in main() starts as: " + str(die1))
    print(f"Simulating {NUM_ROLLS} dice rolls:\n")
    # roll_dice()
    # roll_dice()
    # roll_dice()
    for i in range(NUM_ROLLS):
        print(f"Roll {i + 1}:")
        roll_dice()
        
    #print("die1 in main() is: " + str(die1))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
