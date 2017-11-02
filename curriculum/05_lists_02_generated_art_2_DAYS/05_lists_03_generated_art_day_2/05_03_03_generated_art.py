from tkinter import *
from random import randint

# add any shapes here that you wish to be part of the drawing from the start
drawList = []

canvasWidth = 200
canvasHeight = 200

def makeIterativeArt():
  while (True):
    print('What would you like to add to the drawing?')
    print('(examples: "red rectangle", "blue oval")')
    print('type "ready" when you are ready to view your creation.')

    drawCommand = input("> ")
    if (drawCommand == "ready"):
      break

    processDrawCommand(drawCommand)

  print("Click the python application icon if you don't see the drawing!")
  runDrawing()

def processDrawCommand(drawCommand):
  # the .split() function turns a string of words (with spaces in between)
  # into a list of words of separate elements.
  # example: "fee fi fo fum".split() becomes ["fee", "fi", "fo", "fum"]
  drawCommandList = drawCommand.split()
  (color, shape) = (drawCommandList[0], drawCommandList[1])
  drawList.append((color, shape))

def draw(canvas, cw, ch):
  for drawCommand in drawList:
    if len(drawCommand) == 6:
      (x0, y0, x1, y1, color, shape) = drawCommand
    else:
      (color, shape) = drawCommand
      (x0, y0, x1, y1) = getRandomSquareCoordinates(canvasWidth, canvasHeight)
    if shape == "rectangle":
      canvas.create_rectangle(x0, y0, x1, y1, fill=color)
    elif shape == "oval":
      canvas.create_oval(x0, y0, x1, y1, fill=color)
    else:
      print("Couldn't draw:", drawCommand)

def getRandomSquareCoordinates(cw, ch):
  squareWidth = 10
  x0 = randint(0, cw-squareWidth)
  y0 = randint(0, ch-squareWidth)
  x1 = x0 + squareWidth
  y1 = y0 + squareWidth
  return (x0, y0, x1, y1)

def runDrawing(width=canvasWidth, height=canvasHeight):
  root = Tk()
  canvas = Canvas(root, width=width, height=height, highlightthickness=0)
  canvas.pack()
  draw(canvas, width, height)
  root.mainloop()

makeIterativeArt()

# Challenge 2.1 - Run the file to get an idea of what it does.
#    Then make it much cooler by making the shape width and height random as well.
# Hint: You need only change a few lines in getRandomSquareCoordinates.
# Hint: You will need to use: randint(lowNumber, highNumber)

# Challenge 2.2 - Figure out a way to add a third number in each command, like:
#      3 red rectangle
#    That will add 3 red rectangles to the drawList!
# Hint: Read through all the code to understand what it is doing..!
# Hint: You will need to add another element to the tuples.

# BONUS Challenge 2.3 - Wouldn't it be cool to have more shapes to add?
#    Do some research online to find out how to draw at least one of the
#    following:
#    - text (look for "tkinter create_text")
#      Suggested input format: "blue hello" (draws the text "hello" in blue
#      font color in a random position)
#    - triangles (look for "tkinter create_polygon")
#      Suggested input format: "yellow triangle"
#    - your own shape??
#    Hint: You will have to be very creative and make decisions on how you will
#    store the coordinates for each new shape.
