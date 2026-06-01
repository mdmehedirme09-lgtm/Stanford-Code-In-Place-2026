from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    for i in range(3):#fill the first three column first
        fill_column()
        move_to_wall()
        move_to_column()
    fill_column() #for the last column
    move_to_wall()    

def move_to_column():
    #a function to find the column
    for i in range(4):
        move()
def fill_column():
    #fill the column
    turn_left()
    for i in range(4):
        put_beeper()
        move()
    put_beeper()#for the last beeper    
def move_to_wall():
    turn_right()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
def turn_right():
    for i in range(3):
        turn_left()    
if __name__ == '__main__':
    main()
