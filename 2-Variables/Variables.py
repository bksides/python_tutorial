# Hello again!

# Let's go ahead and talk through this program.  The first thing that's happening is that we're getting information from
# the user.  Here's the line that does this:

user = input("Hi!  What's your name? ")

# There's a lot happening in just this line.  Part of it you might recognize; the bit to the right of the equals sign
# is another function call.  Just as the "print" function outputs something to the user, the "input" function gets
# input FROM the user.  It relies on another useful property of functions - sometimes they "return" data that the
# calling program can use.  The "argument" between the parentheses of the function call is the "prompt" - the text the
# user will see before the program waits for their input.  If you recognized this pattern from the last lesson, great!
# That means it's sticking!  If not, that's ok - the goal is to see these things often enough that they are instantly
# recognizable.

# That brings us to the rest of that line.  To the left of the equals sign you see the word "user" - this is the name of
# the variable that we are creating in that line.  You can think of variables as named references to some piece of data
# that allows you to refer back to it later in your code.  They can be named almost anything, with a few restrictions:
# the names can only consist of letters, numbers, and underscores, and they can't begin with a number.  So "name",
# "user_name", and "myUser1" are all valid variable names; "my name", "some-variable", and "999xShadowKillerx999" are
# not.

# It's important to remember that the name of the variable itself has NO MEANING to the interpreter; many new
# programmers agonize over the names of their variables believing that the names they choose will affect the behavior
# of their programs.  This is not the case; it is smart to name your variables according to the data they hold, but only
# because that makes the programs more decipherable to humans.  The interpreter does not care, so long as you refer to
# the variable by the same name throughout your code.  To demonstrate that, you can try changing the name of the
# variable above to any other valid variable name.  The program will still work no matter what you name it - so long as
# you also change the reference to that variable that occurs below!  Again, to reiterate, it does not matter what you
# call your variables, SO LONG AS THE NAME IS CONSISTENT THROUGHOUT THE PROGRAM.

# The `=` is the "assignment operator".  It assigns the value on its right to the variable on its left.  All variables
# are created in this way; <variable name> = <value>.

# Putting all this together, we have a line that:
#   - creates a variable called "user"
#   - receives input from the user
#   - assigns the input it receives from the user to the newly created variable

# Keeping track of data is useless if you don't use it, so let's use it!  We will print a personalized greeting for the
# user:

print("Hello, " + user + "!")

# This is a print statement just like the ones from last lesson, only this time there's some weirdness in the middle
# there.  Rather than just giving print a predefined phrase as an argument, we are building a phrase that includes
# the user's input.  This is done using the `+` operator, which when used on "strings" of characters will combine them
# into a single string.

# As an exercise, let's get to know our user a little better!  Add some extra code below this comment to ask the user
# something about themselves, and print something that shows you retained the information!

# DELETE THIS LINE AND REPLACE IT WITH YOUR CODE!

# What else can we do with this kind of data?  Importantly, how can we use data to control the behavior of our program?
# This will be the focus of the next lesson.