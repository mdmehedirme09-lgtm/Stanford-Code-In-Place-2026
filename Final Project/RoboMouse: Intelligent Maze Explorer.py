from graphics import Canvas
import random
import time



ROWS = 21
COLS = 21
CELL_SIZE = 25

CANVAS_WIDTH = COLS * CELL_SIZE
CANVAS_HEIGHT = ROWS * CELL_SIZE


# ------------------------
# CREATE EMPTY MAZE
# ------------------------

def create_empty_maze():
    maze = []

    for r in range(ROWS):
        row = []

        for c in range(COLS):
            row.append('#')

        maze.append(row)

    return maze


# ------------------------
# DFS MAZE GENERATOR
# ------------------------

def dfs(maze, row, col):

    maze[row][col] = '.'

    directions = [
        (-2, 0),
        (2, 0),
        (0, -2),
        (0, 2)
    ]

    random.shuffle(directions)

    for dr, dc in directions:

        nr = row + dr
        nc = col + dc

        if 1 <= nr < ROWS - 1 and 1 <= nc < COLS - 1:

            if maze[nr][nc] == '#':

                maze[row + dr // 2][col + dc // 2] = '.'

                dfs(maze, nr, nc)


# ------------------------
# ADD LOOPS
# ------------------------

def add_loops(maze, chance=0.15):

    for r in range(1, ROWS - 1):
        for c in range(1, COLS - 1):

            if maze[r][c] == '#':

                if random.random() < chance:

                    maze[r][c] = '.'


# ------------------------
# DRAW MAZE
# ------------------------

def draw_maze(canvas, maze):

    for row in range(ROWS):

        for col in range(COLS):

            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE

            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            if maze[row][col] == '#':
                color = "black"

            elif maze[row][col] == 'S':
                color = "yellow"

            elif maze[row][col] == 'G':
                color = "green"

            else:
                color = "white"

            canvas.create_rectangle(
                x1,
                y1,
                x2,
                y2,
                color
            )


# ------------------------
# DRAW MOUSE
# ------------------------

def draw_mouse(canvas):

    size = CELL_SIZE - 10

    mouse = canvas.create_oval(
        0,
        0,
        size,
        size,
        "blue"
    )

    return mouse


# ------------------------
# GRID TO PIXEL
# ------------------------

def cell_to_pixel(row, col):

    x = col * CELL_SIZE + 5
    y = row * CELL_SIZE + 5

    return x, y


# ------------------------
# FLOOD FILL
# ------------------------

def flood_fill(maze, goal):

    values = []

    for r in range(ROWS):

        row = []

        for c in range(COLS):

            if maze[r][c] == '#':
                row.append(-1)
            else:
                row.append(999)

        values.append(row)

    goal_row, goal_col = goal

    values[goal_row][goal_col] = 0

    changed = True

    while changed:

        changed = False

        for r in range(ROWS):

            for c in range(COLS):

                if values[r][c] == -1:
                    continue

                directions = [
                    (-1, 0),
                    (1, 0),
                    (0, -1),
                    (0, 1)
                ]

                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS:

                        if values[nr][nc] != -1:

                            if values[r][c] > values[nr][nc] + 1:

                                values[r][c] = values[nr][nc] + 1

                                changed = True

    return values


# ------------------------
# GET FLOOD PATH
# ------------------------

def get_flood_path(values, start, goal):

    path = [start]

    row, col = start

    while (row, col) != goal:

        choices = []

        best_value = values[row][col]

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for dr, dc in directions:

            nr = row + dr
            nc = col + dc

            if 0 <= nr < ROWS and 0 <= nc < COLS:

                if values[nr][nc] != -1:

                    if values[nr][nc] < best_value:

                        best_value = values[nr][nc]
                        choices = [(nr, nc)]

                    elif values[nr][nc] == best_value:
                        choices.append((nr, nc))

        row, col = random.choice(choices)

        path.append((row, col))

    return path


# ------------------------
# DRAW FLOOD VALUES
# ------------------------
def draw_values(canvas, values):

    for r in range(ROWS):

        for c in range(COLS):

            if values[r][c] != -1:#-1 refers to presence of wall

                canvas.create_text(
                    c * CELL_SIZE + CELL_SIZE / 2,
                    r * CELL_SIZE + CELL_SIZE / 2,
                    str(values[r][c]),
                    color="purple"
                )


# ------------------------
# ANIMATE MOUSE
# ------------------------

def animate_mouse(canvas, mouse, path):

    current_row, current_col = path[0]

    x, y = cell_to_pixel(current_row, current_col)

    canvas.moveto(mouse, x, y)

    time.sleep(0.5)

    for row, col in path[1:]:

        dx = (col - current_col) * CELL_SIZE
        dy = (row - current_row) * CELL_SIZE

        canvas.move(mouse, dx, dy)

        current_row = row
        current_col = col

        time.sleep(0.08)


# ------------------------
# MAIN
# ------------------------

def main():

    canvas = Canvas(
        CANVAS_WIDTH,
        CANVAS_HEIGHT
    )

    maze = create_empty_maze()

    dfs(maze, 1, 1)

    # ADD EXTRA PATHS
    add_loops(maze, 0.15)

    start = (1, 1)
    goal = (ROWS - 2, COLS - 2)

    start_row, start_col = start
    goal_row, goal_col = goal

    maze[start_row][start_col] = 'S'
    maze[goal_row][goal_col] = 'G'

    values = flood_fill(
        maze,
        goal
    )

    draw_maze(
        canvas,
        maze
    )

    draw_values(
        canvas,
        values
    )

    mouse = draw_mouse(canvas)

    path = get_flood_path(
        values,
        start,
        goal
    )

    animate_mouse(
        canvas,
        mouse,
        path
    )

    print("Maze Solved!")
    


if __name__ == '__main__':
    main()
