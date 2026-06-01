"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    Put 10 beepers in every cell in the bottom row of the world.
    """
    
     # Delete this line and write your code here! :)
    while front_is_clear():
        put10_beeper()
        move()
    put10_beeper()    
def put10_beeper():
    for i in range(10):
        put_beeper()
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
