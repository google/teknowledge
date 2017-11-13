def startTrail():
    print("There are three trails to hike.")
    print("Type red, blue or green to choose your trail.")
    trail = input("> ")

    if trail == "red":
        redTrail()
    elif trail == "blue":
        blueTrail()
    else:
        greenTrail()

    print("The end.")


def redTrail():
    print("You hike the red trail.")
    print("The red trail is adventurous.")


startTrail()

# Challenge 1.1 - What happens if you try to hike the blue trail?
#    Fix it by defining and implementing the greenTrail and blueTrail
#    functions. For each, print strings of your choice!

# Challenge 1.2 - Make another function, chooseTrail, and move the
#    code that assigns the variable trail and the if-elif-else code there.
#    Change startTrail to call chooseTrail two times
#    in a row so you can now hike two different trails.

# BONUS Challenge 1.3 - Make the code allow you to go on an infinite hike...
#    until you input "stop", then it will say "The end." and stop.
# Hint: You will have to have a function call itself! Tricky!
