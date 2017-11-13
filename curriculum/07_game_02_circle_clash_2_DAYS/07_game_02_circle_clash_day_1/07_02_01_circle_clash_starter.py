from tkinter import *


# the game data for the initial game state
def init():
    data.playerX = 550
    data.playerY = 300


# events updating the game data
def keyPressed(event):
    key = event.keysym


# the game data updating the game state
def timerFired():
    pass  # do something here


# the game state updating what is drawn
def redrawAll(canvas):
    canvas.create_text(300, 250, text="Not Yet A Game", font=" Arial 20")


# Challenge 1.1 - Draw a little red circle using the playerX and playerY
#    coordinates.

# Challenge 1.2 - Make it so the left and right keyboard keys move the little
#    red circle left and right.

# Challenge 1.3 - Make a big yellow circle that falls down the screen from the
#    top of the screen.

# Challenge 1.4 - Make it so when the circles collide the text "Game Over"
#    appears.
#    Hint: Use the distance formula, like the playerAtWinSpot() function from
#    last week.


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
    data.timerDelay = 200  # milliseconds
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
