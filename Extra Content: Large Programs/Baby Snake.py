from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # TODO: your code here
    # Player starts in top-left corner
    player = canvas.create_rectangle(
        0, 0,
        SIZE, SIZE,
        "blue"
    )

    # Goal starts somewhere on the grid
    goal = canvas.create_rectangle(
        360, 360,
        380, 380,
        "red"
    )

    direction = "Right"

    while True:

        # Handle keyboard input
        key = canvas.get_last_key_press()

        if key == "ArrowLeft":
            direction = "Left"
        elif key == "ArrowRight":
            direction = "Right"
        elif key == "ArrowUp":
            direction = "Up"
        elif key == "ArrowDown":
            direction = "Down"

        # Move player
        if direction == "Right":
            canvas.move(player, SIZE, 0)

        elif direction == "Left":
            canvas.move(player, -SIZE, 0)

        elif direction == "Up":
            canvas.move(player, 0, -SIZE)

        elif direction == "Down":
            canvas.move(player, 0, SIZE)

        # Get player position
        player_x = canvas.get_left_x(player)
        player_y = canvas.get_top_y(player)

        # Check if out of bounds
        if (
            player_x < 0 or
            player_y < 0 or
            player_x >= CANVAS_WIDTH or
            player_y >= CANVAS_HEIGHT
        ):
            print("Game Over!")
            break

        # Get goal position
        goal_x = canvas.get_left_x(goal)
        goal_y = canvas.get_top_y(goal)

        # Collision with goal
        if player_x == goal_x and player_y == goal_y:

            new_x = random.randint(0, (CANVAS_WIDTH // SIZE) - 1) * SIZE
            new_y = random.randint(0, (CANVAS_HEIGHT // SIZE) - 1) * SIZE

            canvas.moveto(goal, new_x, new_y)

        time.sleep(DELAY)

if __name__ == '__main__':
    main()
