from tkinter import *
from random import randint

# the game data for the initial game state
def init():
  data.playerX = 250
  data.playerY = 550
  data.circleX = 250
  data.circleY = 0
  data.gameOver = False

# events updating the game data
def keyPressed(event):
  if event.keysym == "Right" and data.playerX < 550:
    data.playerX += 5
  elif event.keysym == "Left" and data.playerX > 0:
    data.playerX -= 5

def moveCircle():
  if not data.gameOver:
    data.circleY += 10

# the game data updating the game state
def timerFired():
  moveCircle()
  if checkCollision(data.playerX, data.playerY,
                    data.circleX, data.circleY,
                    10, 50):
    data.gameOver = True
  if data.circleY > 600:
    data.gameOver = True

def checkCollision(x1, y1, x2, y2, r1, r2):
  distance = ((x2-x1)**2 + (y2 - y1)**2)**0.5
  return distance <= r1 + r2

# the game state updating what is drawn
def redrawAll(canvas):
  canvas.create_oval(data.playerX - 10, data.playerY - 10,
                     data.playerX + 10, data.playerY + 10,
                     fill="red")
  canvas.create_oval(data.circleX - 50, data.circleY - 50,
                     data.circleX + 50, data.circleY + 50,\
                     fill="yellow")
  if data.gameOver:
    canvas.create_text(300, 250, text="Game Over", font=" Arial 20")


# Challenge 2.1 - Make it so that at the top of the screen it says "Score: __"
#    where the __ is a number that increases every time timerFired() happens.

# Challenge 2.2 - Make it so that every third time timerFired() happens a new
#    circle is added to the top of the screen with random x position, color,
#    and size.
#    Suggested way to do this:
#      1. Make a data.timer variable that starts at 0 and increases by 1 every
#         timerFired() and a data.circles variable that starts as [].
#      2. When data.timer gets to 3, reset it to 0 and call a new function
#         createNewCircle().
#      3. Write createNewCircle() to append a tuple to data.circles of the
#         format:
#           (xCoordinate, yCoordinate, radiusSize, colorString)
#      4. In redrawAll(), loop over the data.circles list and draw each circle.
#      5. In timerFired(), every second, move each circle's yPosition down by
#         10 pixels.

# BONUS Challenge 2.3 - Make the game better with your own ideas!
#    The coding world is now yours for the exploring :)


# ***** DO NOT MODIFY BELOW HERE ***** #

# animation setup code

class Struct(object): pass
data = Struct()

def run(width=600, height=600):
  def redrawAllWrapper(canvas):
    canvas.delete(ALL)
    redrawAll(canvas)
    canvas.update()    

  def keyPressedWrapper(event, canvas):
    keyPressed(event)
    redrawAllWrapper(canvas)

  def timerFiredWrapper(canvas):
    timerFired()
    redrawAllWrapper(canvas)
    # pause, then call timerFired again
    canvas.after(data.timerDelay, timerFiredWrapper, canvas)

  # Set up data and call init
  data.width = width
  data.height = height
  data.timerDelay = 200 # milliseconds
  init()
  # create the root and the canvas
  root = Tk()
  canvas = Canvas(root, width=data.width, height=data.height)
  canvas.pack()
  # set up events
  root.bind("<Key>", lambda event:
                          keyPressedWrapper(event, canvas))
  timerFiredWrapper(canvas)
  # and launch the app
  root.mainloop()  # blocks until window is closed
  print("bye!")

run()
