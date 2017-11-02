# ^_^ WEEK 03 FUN ^_^
# TAKE-HOME CHALLENGE
from tkinter import *

def draw(canvas, width, height):
  # Fun: For more interesting colors, visit: http://wiki.tcl.tk/37701
  fillColor = "blue"
  canvas.create_rectangle(0, 0, 10, 10, fill=fillColor)
  canvas.create_rectangle(10, 10, 20, 20, fill=fillColor)
  canvas.create_rectangle(20, 20, 30, 30, fill=fillColor)

def runDrawing(width=200, height=200):
  root = Tk()
  canvas = Canvas(root, width=width, height=height, highlightthickness=0)
  canvas.pack()
  draw(canvas, width, height)
  root.mainloop()
  print("bye!")

runDrawing()

# Challenge fun.1 - Run the function to see what it does. Note the diagonal.
#    Use a *loop* (for loop or while loop) to complete the diagonal of squares.

# Challenge fun.2 - Make another diagonal next to the original one with a
#    different color.
# Hint: You can use the same loop or a separate loop.

# BONUS Challenge fun.3 - Make the entire screen a checkerboard pattern!
