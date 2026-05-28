from graphics import Canvas
import math
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

# Smaller trees
TRUNK_HEIGHT = 50
TRUNK_WIDTH = 15
LEAVES_SIZE = 40

# Move trees slightly upward
TREE_BOTTOM_Y = CANVAS_HEIGHT - 40

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Clouds
    draw_cloud(canvas, 140, 10, 'salmon')
    draw_cloud(canvas, 20, 60, 'pink')
    draw_cloud(canvas, 260, 40, 'purple')

    # Trees
    draw_tree(canvas, 40, "green")
    draw_tree(canvas, 100, "red")
    draw_tree(canvas, 280, "orange")


def draw_cloud(canvas, x, y, color):

    cloud_bottom_start_y = y + (1/3) * CLOUD_HEIGHT
    cloud_bottom_end_y = y + CLOUD_HEIGHT

    cloud_top_start_x = x + (1/4) * CLOUD_WIDTH
    cloud_top_end_x = x + (3/4) * CLOUD_WIDTH

    # Bottom left puff
    canvas.create_oval(
        x,
        cloud_bottom_start_y,
        x + (3/4) * CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )

    # Bottom right puff
    canvas.create_oval(
        x + (1/4) * CLOUD_WIDTH,
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )

    # Top puff
    canvas.create_oval(
        cloud_top_start_x,
        y,
        cloud_top_end_x,
        y + (2/3) * CLOUD_HEIGHT,
        color
    )


def draw_tree(canvas, x, color):

    # Leaves
    leaves_top_y = TREE_BOTTOM_Y - TRUNK_HEIGHT - LEAVES_SIZE

    canvas.create_oval(
        x,
        leaves_top_y,
        x + LEAVES_SIZE,
        leaves_top_y + LEAVES_SIZE,
        color
    )

    # Trunk
    trunk_x = x + LEAVES_SIZE / 2 - TRUNK_WIDTH / 2

    canvas.create_rectangle(
        trunk_x,
        TREE_BOTTOM_Y - TRUNK_HEIGHT,
        trunk_x + TRUNK_WIDTH,
        TREE_BOTTOM_Y,
        "brown"
    )


if __name__ == '__main__':
    main()
