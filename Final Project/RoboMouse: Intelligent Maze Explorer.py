from graphics import Canvas
import random
import time

ROWS = 21
COLS = 21
CELL_SIZE = 25

CANVAS_WIDTH = COLS * CELL_SIZE
CANVAS_HEIGHT = ROWS * CELL_SIZE

#create empty maze

def empty_maze():
    
    '''
     Lets create an empty list &
     later we append row to this list &
     this become 2d array with rows & columns
     '''
    maze=[]#empty list
    for r in range(ROWS):
        row=[]
        for c in range(COLS):
            row.append("#")
        maze.append(row)

    return maze

#this function creates a random maze every run
def dfs_maze(maze,row,col):
    maze[row][col]='.'
    direction=[ (2,0), #2 step right
                (0,2), #2 step down
                (-2,0),#2 step left
                (0,-2)#2 step up
              ]
    #Randomly shuffling the direction every time when the programme runs
    random.shuffle(direction)
    for r,c in direction:
        new_row=row+r
        new_col=col+c
        if 1<=new_row<=ROWS-2 and 1<=new_col<=COLS-2:#check the cell is inside the boundary
            if maze[new_row][new_col]=="#":#check while the cell is unvisited
                maze[row+r//2][col+c//2]='.'#clear the wall
                dfs_maze(maze,new_row,new_col)#Reccursive call to the function


#we add afunction that the mouse faces multiple paths 
def multiple_paths(maze,chance=0.15):
    for r in range(1,ROWS-1):
        for c in range(1,COLS-1):
            if maze[r][c]=="#":
                if random.random()<chance:
                    maze[r][c]='.'#

#we draw the maze using graphics library

def draw_maze(canvas,maze):
    for r in range(ROWS):
        for c in range(COLS):
            x_start=c*CELL_SIZE
            y_start=r*CELL_SIZE
            x_end=x_start+CELL_SIZE
            y_end=y_start+CELL_SIZE

            if maze[r][c]=="#":
                color="Black"
            elif maze[r][c]=="S":
                color="Yellow"
            elif maze[r][c]=="G":
                color="Green"
            else:
                color="White"

            canvas.create_rectangle(x_start,
                                    y_start,
                                    x_end,
                                    y_end,
                                    color
            )


def draw_mouse(canvas):
    size=CELL_SIZE-10
    mouse=canvas.create_oval(0,0,size,size,color="blue")

    return mouse

'''
we need to convert the coordinates to
pixel because canvas uses pixel coordinates
'''
def make_pixel(row,col):
    x=col*CELL_SIZE+5
    y=row*CELL_SIZE+5

    return x,y 

'''
We implement flood fill Algorithm
in order to find the distance of 
every cell from the goal cell
'''

def flood_fill(maze,goal):
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

#this function helps mouse to moves along the flood fill path
def get_flood_fill_path(value,start,goal):
    path=[start]
    r,c=start
    while(r,c)!=goal:
        choices=[]
        best_value=value[r][c]
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
                if value[nr][nc] != -1:
                    if value[nr][nc] < best_value:
                        best_value = value[nr][nc]
                        choices = [(nr, nc)]
                    elif value[nr][nc] == best_value:
                        choices.append((nr, nc))
    
        r,c = random.choice(choices)
        path.append((r, c))
    return path

#draw values to each cell according to flood fill algorithm that the mouse choice for move
def draw_values(canvas, values):
    for r in range(ROWS):
        for c in range(COLS):
            if values[r][c] != -1:#-1 refers to presence of wall
                canvas.create_text(
                    c * CELL_SIZE + CELL_SIZE / 2,
                    r * CELL_SIZE + CELL_SIZE / 2,
                    str(values[r][c]),
                    color="maroon"
                )

#We use animation to see the mouse movement
def animate_mouse(canvas, mouse, path):
    current_row, current_col = path[0]
    x, y = make_pixel(current_row, current_col)
    canvas.moveto(mouse, x, y)
    time.sleep(0.5)

    for row, col in path[1:]:
        dx = (col - current_col) * CELL_SIZE
        dy = (row - current_row) * CELL_SIZE
        canvas.move(mouse, dx, dy)
        current_row = row
        current_col = col

        time.sleep(0.08)


#finally the main function where we call the above function
def main():
    canvas = Canvas(CANVAS_WIDTH,CANVAS_HEIGHT)
    maze = empty_maze()
    dfs_maze(maze, 1, 1)
    # ADD EXTRA PATHS
    multiple_paths(maze, 0.15)

    start = (1, 1)
    goal = (ROWS - 2, COLS - 2)
    start_row, start_col = start
    goal_row, goal_col = goal

    maze[start_row][start_col] = 'S'
    maze[goal_row][goal_col] = 'G'

    values = flood_fill(maze,goal)
    draw_maze( canvas,maze)
    draw_values(canvas,values)
    mouse = draw_mouse(canvas)
    path = get_flood_fill_path(values,start,goal)
    animate_mouse(canvas,mouse,path)

    print("Maze Solved!")
    

if __name__ == '__main__':
    main()
