import turtle

def save_as_jpg(canvas, fileName):
    # same as before
     ...

def drawRectangle(ttl, x, y, width, height):
    """Draw a rectangle of dimensions width and height, with upper left corner at (x, y)."""
    ttl.up()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.down()
    for i in range(2):
        ttl.forward(width)
        ttl.right(90)
        ttl.forward(height)
        ttl.right(90)

def drawTriangle(ttl, x1, y1, x2, y2, x3, y3):
    """Draw a triangle."""
    ttl.penup()
    ttl.goto(x1, y1)
    ttl.pendown()
    ttl.goto(x2, y2)
    ttl.goto(x3, y3)
    ttl.goto(x1, y1)

def fillTriangle(ttl, x1, y1, x2, y2, x3, y3, color):
    """Fill a triangle with color, given as hex string value."""
    ttl.fillcolor(color)
    ttl.begin_fill()
    drawTriangle(ttl, x1, y1, x2, y2, x3, y3)
    ttl.end_fill()

# Set up the screen size (in pixels ~ 1000 x 1000)
# Set the starting point of the turtle to (0, 0)
turtle.setup(1500, 1000, 0, 0)

myBlue = "#003DA5"
myYellow = "#FFD100"
myRed = "#CF142B"
myGreen = "#007A33"
myWhite = "#FFFFFF"

Joe = turtle.Turtle()
Joe.screen.colormode(255)

drawRectangle(Joe, 0, 300, 600, 300)
Joe.goto(0, 0)

# Draw blue triangle
fillTriangle(Joe, 0, 0, 0, 300, 200, 300, myBlue)

# Draw yellow triangle
fillTriangle(Joe, 0, 0, 200, 300, 400, 300, myYellow)

# Draw red triangle
fillTriangle(Joe, 0, 0, 400, 300, 600, 300, myRed)

# Draw white triangle
fillTriangle(Joe, 0, 0, 600, 300, 600, 150, myWhite)

# Draw green triangle
fillTriangle(Joe, 0, 0, 600, 150, 600, 0, myGreen)

Joe.hideturtle()

ts = turtle.getscreen()
tc = ts.getcanvas()

# Create a PostScript image file
tc.postscript(file="SeychellesFlag.eps")

# Converts to JPEG
save_as_jpg(tc, "SeychellesFlag")

turtle.done()