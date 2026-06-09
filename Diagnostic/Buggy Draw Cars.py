from graphics import Canvas

def main():
    # draws two cars
    canvas = Canvas(400, 400)
    x = 10
    y = 10
    draw_car(canvas,x,y)#pass canvas & x,y also beacuse we dont define x,y in the draw car function

    x = 100
    y = 100
    draw_car(canvas,x,y)

def draw_car(canvas,x,y): #wee need to pass the canvas through this function
    # draws a car at the location x, y
    # you can assume that math offsets for the rectangles are correct
    canvas.create_rectangle(x, y, x + 50, y + 20)
    canvas.create_rectangle(x + 10, y - 10, x + 40, y + 20)

if __name__ == '__main__':
    main()
