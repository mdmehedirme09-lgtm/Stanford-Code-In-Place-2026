from graphics import Canvas
import time
import random
import math

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 600
PADDLE_Y = CANVAS_HEIGHT - 30
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 15
BALL_RADIUS = 10

BRICK_GAP = 5
BRICK_WIDTH = (CANVAS_WIDTH - BRICK_GAP*9) / 10
BRICK_HEIGHT = 10

BRICK_ROWS = 10
BRICK_COLS = 10



DELAY = 0.01


def create_bricks(canvas):
    colors = [
        "red", "red",
        "orange", "orange",
        "yellow", "yellow",
        "green", "green",
        "cyan", "cyan"
    ]

    start_x = (CANVAS_WIDTH - (BRICK_COLS * BRICK_WIDTH +
                               (BRICK_COLS - 1) * BRICK_GAP)) / 2

    start_y = 50

    count = 0

    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLS):

            x = start_x + col * (BRICK_WIDTH + BRICK_GAP)
            y = start_y + row * (BRICK_HEIGHT + BRICK_GAP)

            canvas.create_rectangle(
                x,
                y,
                x + BRICK_WIDTH,
                y + BRICK_HEIGHT,
                colors[row]
            )

            count += 1

    return count


def create_paddle(canvas):
    x = (CANVAS_WIDTH - PADDLE_WIDTH) / 2

    return canvas.create_rectangle(
        x,
        PADDLE_Y,
        x + PADDLE_WIDTH,
        PADDLE_Y + PADDLE_HEIGHT,
        "black"
    )


def create_ball(canvas):
    x = CANVAS_WIDTH / 2 - BALL_RADIUS
    y = CANVAS_HEIGHT / 2 - BALL_RADIUS

    return canvas.create_oval(
        x,
        y,
        x + BALL_RADIUS * 2,
        y + BALL_RADIUS * 2,
        "blue"
    )


def get_collision(canvas, ball):
    x = canvas.get_left_x(ball)
    y = canvas.get_top_y(ball)

    size = BALL_RADIUS * 2

    objects = canvas.find_overlapping(
        x,
        y,
        x + size,
        y + size
    )

    for obj in objects:
        if obj != ball:
            return obj

    return None

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO: your code here
    bricks_left = create_bricks(canvas)

    paddle = create_paddle(canvas)

    lives = 3

    while lives > 0 and bricks_left > 0:

        ball = create_ball(canvas)

        change_x = random.choice([-4, -3, 3, 4])
        change_y = 4

        turn_over = False

        while not turn_over and bricks_left > 0:

            # Move paddle
            mouse_x = canvas.get_mouse_x()

            paddle_x = mouse_x - PADDLE_WIDTH / 2

            if paddle_x < 0:
                paddle_x = 0

            if paddle_x > CANVAS_WIDTH - PADDLE_WIDTH:
                paddle_x = CANVAS_WIDTH - PADDLE_WIDTH

            canvas.moveto(paddle, paddle_x, PADDLE_Y)

            # Move ball
            canvas.move(ball, change_x, change_y)

            x = canvas.get_left_x(ball)
            y = canvas.get_top_y(ball)

            size = BALL_RADIUS * 2

            # Left/right wall
            if x <= 0 or x + size >= CANVAS_WIDTH:
                change_x = -change_x

            # Top wall
            if y <= 0:
                change_y = -change_y

            # Bottom wall = lose life
            if y + size >= CANVAS_HEIGHT:
                lives -= 1
                canvas.delete(ball)
                turn_over = True
                continue

            # Collision detection
            collider = get_collision(canvas, ball)

            if collider is not None:

                if collider == paddle:

                    # Prevent sticky paddle bug
                    if change_y > 0:
                        change_y = -change_y

                else:
                    canvas.delete(collider)
                    change_y = -change_y
                    bricks_left -= 1

            time.sleep(DELAY)

    if bricks_left == 0:
        print("YOU WIN!")
    else:
        print("GAME OVER")

if __name__ == '__main__':
    main()
