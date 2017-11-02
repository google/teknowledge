# ^_^ WEEK 02 FUN ^_^
# TAKE-HOME CHALLENGE

def startGame():
  print("This is an adventure game.")
  input("Press enter to continue the text.")
  print("When you see this you will need to respond. Here type 'ok'. Then press enter.")
  input("> ")
  input("Ready? ...")
  startRoom()

def startRoom():
  input("You are in a big empty room.")
  input("There are two doors.")
  input("Which door do you enter?")
  print("Type 1 or 2 or something else then press enter.")

  door = input("> ")

  if door == "1":
    input("It was a TRAP door.")
    gameOver()
  elif door == "2":
    input("You won right away.  Wow.")
    win() 
  else:
    input("that's not a door, try again.")
    print()
    startRoom()

def win():
  input("You win!!")
  print("congrats :D")

def gameOver():
  print("Game Over!")

startGame()

# FINAL Challenge 2.1 - Your final open-ended challenge today: change this
#    "starter code" to make your own adventure!!

# NOTE: Play and look at the file "02_adventure_example.py" for a longer
#    example to get inspired.
