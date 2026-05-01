from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""
# Stanford Karel: Unit 12: Lesson 1
# Karel finds the midpoint in the world. It is not the center.

# Stanford Karel: Unit 12: Lesson 1
# Karel finds the midpoint in the world. It is not the center.
# Stanford Karel: Unit 12: Lesson 1
# Karel finds the midpoint in the world. It is not the center.



def main():
    mark_walls()
    put_beepers_down()
    turn_around()
    move()
    put_beeper()
    turn_around()
    go_to_wall()
    turn_around()
    last_beeper_standing()
    stay_with_beeper()
#karel saty with beepers in the middle column    
def stay_with_beeper():
    turn_around()
    while no_beepers_present():
        move()
    
    if not_facing_east():
        turn_around()    

# Karel moves to end walls, marking them with beepers
def mark_walls():
    go_to_wall()
    put_beeper()
    turn_around()
    go_to_wall()
    put_beeper()
    turn_around()
    move()
#karel moves until find a block infron of it
def go_to_wall():
    while front_is_clear():
        move()

# Karel starts putting beepers down to find the midpoint of the world.
def put_beepers_down():
    while no_beepers_present():
        move()
        if beepers_present():
            turn_around()
            move()
            put_beeper()
            move()
#karel find the last beeper
def last_beeper_standing():
    while front_is_clear():
        if beepers_present():
            pick_beeper()
        move()
    pick_beeper()

#karel rotates 180 degree 
def turn_around():
    turn_left()
    turn_left()



if __name__ == '__main__':
    main()
