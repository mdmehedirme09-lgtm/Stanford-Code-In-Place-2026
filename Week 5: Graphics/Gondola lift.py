"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from graphics import Canvas
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SQUARE_SIZE = 40
DELAY = 0.01
NUM_STEPS = 500

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    lift_left_x = 0
    lift_bottom_y = CANVAS_HEIGHT - 50
    
    # note these helpful variables!
    lift_width = CANVAS_WIDTH
    lift_height = lift_bottom_y
    
    canvas.create_line(
        lift_left_x, lift_bottom_y,
        lift_left_x + lift_width, lift_bottom_y - lift_height)

    gondola = canvas.create_rectangle(
        0, lift_bottom_y, 
        SQUARE_SIZE, lift_bottom_y + SQUARE_SIZE)

    x = 0
    y = lift_bottom_y

    dx = lift_width / NUM_STEPS
    dy = lift_height / NUM_STEPS

    for step_num in range(NUM_STEPS):
        x += dx
        y -= dy

        canvas.moveto(gondola, x, y)

        time.sleep(DELAY)
       


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
