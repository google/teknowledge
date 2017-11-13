def add(x, y):
    return x + y


def crunchNumbers():
    print("How do you want me to crunch two numbers? ")
    crunchFunction = input("Type add or something else: ")

    num1 = input('First number: ')
    num2 = input('Second number: ')

    if crunchFunction == "add":
        answer = add(num1, num2)
    elif crunchFunction == "subtract":
        answer = subtract(num1, num2)
    else:
        print("That's not a valid crunch method!")
        return

    print("The answer is", answer)


crunchNumbers()

# Challenge 2.1 - Run the code.  The add function doesn't work right! Why is
#    that? Fix it by using the built-in Python int() function.
#    Hint: To see what the int() function can do, try these in Python:
#      int("5")
#      int(5.5)
#      int(3)

# Challenge 2.2 - The subtract function is missing! Add it.

# Challenge 2.3 - Add a function called difference(x, y) that is like subtract
#    but always returns the _positive_ difference between the numbers.
#    Hint: You can use an if statement that uses the "greater than" comparison:
#      if (x > y):

# BONUS Challenge 2.4 - Google search "Python math operators" and see if you
#    can add these three new "crunch functions":
#      - power(x, y) (which takes x to the power of y)
#      - stringAdd(x, y) (which adds the numbers as strings, like add used to)
#        Hint: You'll need the str() function, which turns str("5") -> 5
#      - greatestValue(x, y, z) (which returns the greatest value of all 3)
#        Hint: for greatestValue, you'll need to optionally take a third number
#              as an input
