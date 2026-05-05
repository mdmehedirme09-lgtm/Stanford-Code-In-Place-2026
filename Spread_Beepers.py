from karel.stanfordkarel import *

"""
Each row starts with a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers in
her bag. How can you solve this puzzle?
"""
def main():
    move()
    spread()
    move_to_start()


def spread():
    while beepers_present():
        pick_beeper() # karel can only pick 
        if beepers_present():
            move_to_next()
            put_beeper()
            move_to_start()
            move()
    put_beeper()

def turn_back():
    turn_left()
    turn_left()

def move_to_start():
    turn_back()
    while front_is_clear():
        move()
    turn_back()
    
def move_to_next():
    while beepers_present():
        move()   


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
