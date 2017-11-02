# RUN this file for an example adventure.
# THEN go to 02_my_adventure.py to make your own!

from random import randint

def startGame():
  print("This is an adventure game.")
  input("Press enter to continue the text.")
  print("When you see this you will need to respond. Here type 'ok'. Then press enter.")
  input("> ")
  input("Ready? ...")
  startRoom()

def startRoom():
  input("You are in a big empty room.")
  input("There are four doors.")
  input("Which door do you enter?")
  print("Type 1, 2, 3, or 4 then press enter.")

  door = input("> ")

  if door == "1":
    input("You walk through door 1.")
    emptyRoom()
  elif door == "2":
    input("You walk through door 2.")
    mathTrap()    
  elif door == "3":
    input("You walk through door 3.")
    library()
  elif door == "4":
    pit()
  else:
    input("that's not a door, try again.")
    print()
    startRoom()

def emptyRoom():
  input("It is an empty room.")
  input("But you hear a mysterious voice.")
  input("It whispers:")
  input('"The password is...password..."')
  input("...")
  input("Whatever.  Press enter leave back to the main room.")
  startRoom()

def mathTrap():
  input("OH NO it is a math trap.")
  num1 = randint(1, 99)
  num2 = randint(1, 99)
  stringNum1 = str(num1)
  stringNum2 = str(num2)

  print("Answer the math question correctly to escape:")
  answer = input(stringNum1 + " + " + stringNum2 + " = ")
  if (int(answer) == num1 + num2):
    input("CORRECT!")
    input("You escape back to the main room.")
    startRoom()
  else:
    input("INCORRECT!")
    gameOver()

def library():
  input("You are in a library.")
  input("The librarian glares at you.")
  input("'What is the password?' she asks.")
  print("What do you say?")

  password = input("> ")

  if password == "password":
    input("'How did you know?? Okay then...'")
    input("She pulls a book out of a shelf, then the shelf moves...")
    secretPassage()
  else:
    input("'Incorrect!!' she screams, then kicks you out.")
    startRoom()

def pit():
  input("What is in door 4???")
  print("Guess!")
  input("Your guess: ")
  input("Nope, it's just a bottomless pit.  Sorry.")
  gameOver()

def secretPassage():
  input("You enter a secret passageway.")
  input("and there is cake!")
  win()

def win():
  input("You win!!")
  print("congrats :D")

def gameOver():
  print("Game Over!")

startGame()
