"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    
      # Delete this line and write your code here! :)
    while beepers_present():
        follow_straight_tail()
        step_backwards()
        turn_left()
        move()
        if no_beepers_present():
            step_backwards()
            turn_around()
            move()
def follow_straight_tail():
    while beepers_present():
        pick_beeper()
        move()
def step_backwards():
    turn_around()
    move()
    turn_around()  
def turn_around():
    turn_left()
    turn_left()      
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
