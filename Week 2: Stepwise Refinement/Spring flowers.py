"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    Karel starts in the bottom left corner of a world with 2 empty flower stems, facing East.
    Karel should bloom both flowers with beepers and end in the bottom right corner of the world facing East.
    """
    
    for i in range(2):
        move_to_wall()
        bloom_flower()
    move_to_wall()
def move_to_wall():
    while front_is_clear():
        move()

def bloom_flower():
    climb_up()
    make_bloom()
    move_to_wall()
    turn_left()
def climb_up():
    turn_left()
    while right_is_blocked():
        move()
def make_bloom():
    put_beeper()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    

def turn_right():
    for i in range(3):
        turn_left()        
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
