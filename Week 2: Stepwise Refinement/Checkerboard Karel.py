from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""



def main():
    put_beeper()
    check_wall()
    while front_is_clear():
        beepers_east()
        beepers_west()
    # After finishing the checkerboard, return to (0,0)
    go_home()

def beepers_east():
    while facing_east():
        move()
        if front_is_clear():
            move()
            put_beeper()
        up_east()

def up_east():
    if front_is_blocked():
        if no_beepers_present():
            turn_left()
            if front_is_clear():
                move()
                turn_left()
                put_beeper()
        else:
            turn_left()
            if front_is_clear():
                move()
                turn_left()
                move()
                put_beeper()

def beepers_west():
    while facing_west():
        move()
        if front_is_clear():
            move()
            put_beeper()
        up_west()

def up_west():
    if front_is_blocked():
        if no_beepers_present():
            turn_right()
            if front_is_clear():
                move()
                turn_right()
                put_beeper()
        else:
            turn_right()
            if front_is_clear():
                move()
                turn_right()
                move()
                put_beeper()

def check_wall():
    if front_is_blocked():
        turn_left()
        while front_is_clear():
            move()
            if front_is_clear():
                move()
                put_beeper()

#  New helper: return Karel to (0,0)
def go_home():
    # Face south and go to bottom
    while not_facing_south():
        turn_left()
    while front_is_clear():
        move()
    # Face west and go to left wall
    while not_facing_west():
        turn_left()
    while front_is_clear():
        move()
    # Face east at the end
    while not_facing_east():
        turn_left()

# Helper functions
def turn_right():
    turn_left()
    turn_left()
    turn_left()


                
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
