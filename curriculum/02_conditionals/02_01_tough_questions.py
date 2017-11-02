
input("Press enter to play a game.")

print("In this game, I will ask you a tough question.")
input("Press enter to accept the challenge.")

print("What is 6 times 9?")
print("Type your answer then press enter.")

yourAnswer = input("> ")
realAnswer = "42"


if (yourAnswer == realAnswer):
  print("Right! :-)")
else:
  print("Wrong, you lose.")


# Challenge 2.1 - Play the game - what is wrong?
# Change the code to be correct (can be the answer or the question or both).

# Challenge 2.2 - Add two more questions to the game!



# Place '#' at the beginning of the lines of code above to comment them out


# Remove the '#' in the beginning of the lines of code below



#input("Press enter to play a game.")

#print("In this game, I will ask you a tough question.")
#input("Press enter to accept the challenge.")

#print("What is your favorite color?")
#favColor = input("> ")

#if favColor == 'red':
#  print("Cool your favorite color is red!")
#elif favColor != 'blue':
#  print("Your favorite color isn't blue or red, it is " + favColor + ".")
#else:
#  print("Wow, your favorite color is blue!")


# Challenge 2.3 - What do you think this program will print if your favorite
#   color is blue?  What will it print for purple?  Run the code to see.

# Challenge 2.4 - Change it so it prints a new, special message for purple.
#   Hint: You'll add a new "elif".

# Challenge 2.5 - Let's say we want this program to work if the input starts
#   with a capital letter! So either "blue" or "Blue" should do the same thing,
#   and either "Purple" or "purple" should do the same thing.
#   Hint: Use the "and" or "or" python keywords to accomplish this.

# BONUS Challenge 2.6 - Add a new question below:
#   "How do you spell the color that is a mix of black and white?"
# If their answer is gray (with an a), say:
#   "You must use American English!"
# If their answer is grey (with an e), say:
#   "You must use British English!"
# And in all other cases, say:
#   "Whoops - that's not the color I meant!"
