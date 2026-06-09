from karel.stanfordkarel import *

def main():
    while front_is_clear():
        put_beeper()
        move()
        put_beeper()
        put_beeper_upward()
        if front_is_clear():
            move()
            move()
   
def put_beeper_upward():
    turn_left()
    move()
    put_beeper()
    turn_right()
    turn_right()
    move()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
