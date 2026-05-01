from karel.stanfordkarel import *

#define main function using 5 other function
#We solve it through Decomposition
def main():
    #function_1
    #mark walls by adding beeper beside the two wall
    mark_walls()
    #function_2
    #fill the bottom row with beeper
    put_beepers_down()
    """
    put one more beeper on the middle of the row
    as we later pick all the beeper & the one become remaining!!
    """
    #function_3
    put_one_more_beeper()
    #move untill reach to the wall
    go_to_wall()
    turn_around()
    #function_4
    #pick_bepper from the bottom row once in each column
    last_beeper_standing()
    #function_5
    #At last the karel position over the beeper facing east
    stay_with_beeper()
def mark_walls():
    go_to_wall()
    put_beeper()#at right_most wall
    turn_around()
    go_to_wall()
    put_beeper()#at-left_most wall
    turn_around()
    move()
def put_beepers_down():
    while no_beepers_present():
        move()
        if beepers_present():
            turn_around()
            move()
            put_beeper()
            move()
def put_one_more_beeper():
    turn_around()
    move()
    put_beeper()
    turn_around()   
def last_beeper_standing():
    while front_is_clear():
        if beepers_present():
            pick_beeper()
        move()
    pick_beeper()  
def stay_with_beeper():
    turn_around()
    while no_beepers_present():
        move()
    #force to facing east
    if not_facing_east():
        turn_around()
        #Done                 

def go_to_wall():
    while front_is_clear():
        move()
#rotate the karel by 180 degree
def turn_around():
    turn_left()
    turn_left()        


if __name__ == '__main__':
    main()
