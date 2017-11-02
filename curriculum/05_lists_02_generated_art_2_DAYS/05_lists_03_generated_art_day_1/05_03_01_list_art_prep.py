from tkinter import *
import random

# format of tuples is
# (x0, y0, x1, y1, shapeColor)
# so you can do canvas.create_rectangle(x0, y0, x1, y1, fill=shapeColor)
drawingsList = [
	(0, 0, 20, 20, 'red'),
	(30, 30, 180, 180, 'blue'),
  (110, 20, 140, 190, 'yellow'),
]

def draw(canvas, width, height):
  # YOUR CODE HERE
  drawingTuple = drawingsList[0]
  x0 = drawingTuple[0]
  y0 = drawingTuple[1]
  x1 = drawingTuple[2]
  y1 = drawingTuple[3]
  color = drawingTuple[4]
  canvas.create_rectangle(x0, y0, x1, y1, fill=color)

def getRandomSquareCoordinates(cw, ch):
  pass # your code goes here for Challenge 2.3

def runDrawing(width=200, height=200):
  root = Tk()
  canvas = Canvas(root, width=width, height=height, highlightthickness=0)
  canvas.pack()
  draw(canvas, width, height)
  root.mainloop()
  print("bye!")

runDrawing()

# Challenge 2.1 - For each tuple in the drawingsList, draw a rectangle with the
#    corresponding parameters.  Do this using a loop to loop over each
#    drawingTuple in drawingsList in the draw() function.
#    For example, the tuple at drawingsList[0] draws a red rectangle in the top
#    left corner, like the code is doing now (but do this in a loop).
# Hint: A good way to go about this is to put the current code into a loop,
#    where instead of using drawingsList[0] every time, use each drawingTuple
#    from the list, either by index or by looping over the elements.

# Challenge 2.2 - Add another element to each tuple that is either 'rectangle'
#    or 'oval' and change your draw function to draw the corresponding shape.
#    For example, the drawingTuples will look like:
#      (0, 0, 50, 30, 'black', 'oval')
#    and that would draw a black oval in the top left corner.

# Challenge 2.3 - Write the function, already defined for you above:
#      getRandomSquareCoordinates(cw, ch)
#    which you will call from the draw function, like so:
#      coords = getRandomSquareCoordinates(width, height)
#    and make it so that given a canvas width (cw) and canvas height (ch),
#    the function returns a tuple of coordinates like so:
#      (x0, y0, x1, y1)
#    where the points (x0, y0) and (x1, y1) are the top left and bottom right
#    points of a square, with width 10, that is randomly placed on the canvas.
#       Hint: Use random.randint(0, cw) and random.randint(0, ch)
#    THEN, use this function to draw everything in drawingsList in a random
#    spot!
#    (Note: You can use the same coordinates for drawing both rectangles and
#    ovals.)

# BONUS Challenge - NONE!  (This example continues to the next file.)
