from graphics import Canvas
import random

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO, your code here
    for i in range(BRICKS_IN_BASE):
        for j in range(0,BRICKS_IN_BASE - i):
            start_x = (CANVAS_WIDTH - BRICK_WIDTH * (BRICKS_IN_BASE - i)) / 2 + BRICK_WIDTH * j
            start_y = CANVAS_HEIGHT - BRICK_HEIGHT * (i + 1)
            canvas.create_rectangle(
                start_x,
                start_y,
                start_x+BRICK_WIDTH,
                start_y+BRICK_HEIGHT, 
                "yellow", "black"
                )
           

if __name__ == '__main__':
    main()
