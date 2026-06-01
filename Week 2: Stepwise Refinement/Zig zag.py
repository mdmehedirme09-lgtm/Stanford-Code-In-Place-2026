"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    Places beepers in a zig zag pattern.
    """
    
    # Delete this line and write your code here! :)
    while front_is_clear():
        move_upward()
        move_horizontal()
        move_downward()
def move_upward():
    put_beeper()
    turn_left()
    move()
def move_horizontal():
    turn_right()
    move()
    put_beeper()
    

def turn_right():
    for i in range(3):
        turn_left()
def move_downward():
    turn_right()
    move()
    turn_left()
    if front_is_clear():
        move()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
