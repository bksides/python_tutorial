# You made it!  Welcome to Python!

# You are probably wondering what you're looking at.  A Python file, denoted by the .py extension, is simply a text file
# structured in a way that the Python interpreter knows how to read.  Notice the pound signs (or octothorpes, or number
# signs, or hashtags, or whatever terminology you prefer) at the beginning of each of these lines.  These pound signs
# tell the Python interpreter to ignore these lines, so I don't have to worry about what I type here; the interpreter
# won't read it, so I can say whatever I want!  Hey, Python interpreter!  You're ugly!  Don't worry, it can't hear.

# Comments are a good way to make your code understandable to others, and that's how I'll be using them here.  So how
# about we talk about the line right below this one - the one that doesn't start with a '#'

print("This is a print statement!")

# THAT is a line of bona-fide python code, and when you run this file, that's what the interpreter is reading.  We've
# just told Python to take the phrase we gave it - "This is a print statement!" - and "print" it to the terminal.  Let's
# break it down a little further.

# there are three parts of this line I want us to pay attention to: the word 'print', the parentheses, and the quoted
# part of the line.

# 'print' is the name of a function in Python.  You don't have to worry about what a "function" is just yet - that will
# come later.  For now, just think of them as a kind of command.  There are many functions built into python, and you
# can also define functions yourself.  When we want to use a function in python code, we "call" that function.

# Calling a function is done by typing the name of the function, followed by a pair of parentheses.  Sometimes just the
# pair of parentheses is enough; for instance, the print statement below is perfectly valid:
print()
# but this just prints an empty line.  We want to print a specific phrase.

# For this reason, function calls take "arguments" - extra bits of information that modify the function's behavior.
# These "arguments" go in between the parentheses.  That's what we're doing with our first print statement: We are
# calling the "print" function, with the phrase "This is a print statement!" as an argument!

# Now for an exercise: add an additional print statement below these comments, and have it print "Hello, world!"

# Or have it print whatever you like!  It's your program, after all!

# ERASE THIS LINE AND PUT YOUR PRINT STATEMENT HERE!

# Once you've done this, you can run the python file again.  If all goes well, three lines will appear on your terminal:
#   This is a print statement!
#   
#   Hello, world! (or whatever you had your print statement say)

# The python interpreter goes through programs line by line, executing statements one after the other, so the lines
# appear in the same order you print them in this file.  If you want, you can try re-ordering the print statements - you
# should see that the order of the output lines changes accordingly.

# Congratulations!  You've beaten every programmer's first challenge, the hello world program!  Now it's time to move
# on to the next exercise, where we talk about variables and data types.  Go to the root directory of this project and
# navigate into "2-Variables", or just click the link in the README of this lesson, to continue!