from IMDBDatabase import IMDBData

# GUIDED PRACTICE
# Challenge 1.1 - The first step to data analysis is always to understand the
# database. Just like you can use a for loop to print all the elements in a list,
# use a for loop to print all the movieNames in IMDBData.



# GUIDED PRACTICE
# Challenge 1.2 - Since IMDBData is a dictionary, you can access the data about
# a particular movie with IMDBData["Zootopia"]. Since each movie has a lot of
# data about it, it is also a dictionary. As you did in Challenge 1.1, use a
# for loop to print out all the characteristics that this database stores about
# a particular movie.
#
# Hint: Change the dictionary you are looping over in Challenge 1.1 to instead loop
# over the dictionary IMDBData["Zootopia"]



# GUIDED PRACTICE
# Challenge 1.3 - Great, we now have an understanding of the data that is stored
# in the database! Let's see what that data is. For any one movie in the database,
# print out its stars, rating, genre, and year. An example of getting
# Zootopia's stars is below:
#
# print(IMDBData["Zootopia"]["Stars"])



# GUIDED PRACTICE
# Challenge 1.4 - Now that you understand how the database is structured, let's
# look at the actual database! Open IMDBDatabase.py (NOT .pyc), and look at the
# information stored in the database and how it is structured.

# GUIDED PRACTICE
# Challenge 1.5 - Now let's start answering some questions about these movies.
# For starters, let us determine the highest rated movie in this database. Write
# a loop that goes over all the movies in the database, gets its rating,
# and prints the name and rating of the highest rated movie.
#
# Hint: You will need to have two variables, maxRating and maxRatedMovie,
# that keep track of the highest rated movie you have seen so far.



# Challenge 1.6 - Now let's find the oldest movie in the database. Write a loop
# that goes over every movie in the database, get its year, and ends up printing
# the name and year of the oldest movie.
#
# Hint: Like in Challenge 1.5, you will have to maintain two variables as you
# go through the loop. But this time, they will keep track of the oldestYear you
# have seen so far, and the name of the oldestMovie.



# Challenge 1.7 - Now let's find the number of Animation movies in the database.
# Write a loop that goes over every movie in the database, get its genre, and
# ends up printing the number of Animation movies.
#
# Hint: This time, you will have to maintain one variable, which represents the
# number of Animation movies you have seen so far.



# BONUS Challenge 1.8 - As you saw above, the "Stars" attribute of a movie is a
# list of strings. It contains the names of the actors/actresses in the movie.
# Write a loop that determines how many of the movies in this database "Tom Hanks"
# has acted in.
#
# Hint 1: Like in Challenge 1.5, you will have to loop over the list and have an
# if statement in the loop. But this time, your if statement wants to check
# whether the string "Tom Hanks" is in movieName's stars list.
#
# Hint 2: In Challenge 1.5, you had to keep one variable that keeps track of the
# highest rated movie you have seen so far. Similarly, in this question you
# will have to maintain one variable that keeps track of the number of Tom Hanks
# movies you have encountered so far in your loop.




# BONUS Challenge 1.9 - In Challenge 1.6, you wrote code to determine the number
# of Tom Hanks movies in the database. Now, modify it so that you can type a name in,
# and it will tell you the number of movies by that actor/actress in the database.
#
# Hint: Remember input()?
