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
    comment and replace it with a better, more descriptive one!
    """
    
  # Delete this line and write your code here! :)
    while front_is_clear():
        zebra_crossing()
        if front_is_clear():
            for i in range(4):
                move()
def zebra_crossing():
    ascend_order()
    descend_order()
def ascend_order():
    put_beeper()
    turn_left()
    move()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    turn_right()    
def descend_order():
    move()
    put_beeper()
    turn_right()
    while front_is_clear():
        move()
        put_beeper()
    turn_left()    
def turn_right():
    for i in range(3):
        turn_left()        
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
