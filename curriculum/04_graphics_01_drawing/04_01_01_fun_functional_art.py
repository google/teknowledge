# ^_^ WEEK 04 FUN ^_^
# TAKE-HOME CHALLENGE
from random import randint
from tkinter import *


def drawRectangle(canvas, rectWidth, rectHeight, color):
    # The randint(low, high) function gives you a random number!
    # (If you have the "from random import randint" line at the top.)
    x1 = randint(0, 190)
    y1 = randint(0, 190)
    x2 = x1 + 200
    y2 = y1 + 200
    canvas.create_rectangle(x1, y1, x2, y2, fill="maroon")


def draw(canvas, width, height):
    for i in range(100):
        drawRectangle(canvas, 10, 10, "blue")


def runDrawing(width=200, height=200):
    root = Tk()
    canvas = Canvas(root, width=width, height=height, highlightthickness=0)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("bye!")


runDrawing()

# Challenge fun.1 - Right now, you'll notice the rectWidth, rectHeight, and
#    color parameters are unused. Fix the drawRectangle function so they are
#    used!

# Challenge fun.2 - Make it so the rectWidth and rectHeight numbers are random
#    in drawRectangle!
# Hint: You can delete the parameters after doing that!

# Challenge fun.3 - Make it so the color is random between three random colors
#    in drawRectangle!
# Hint: You can delete the color parameter after.

# BONUS Challenge - Make a new function drawSomething that randomly selects
#    between ovals and rectangles.
