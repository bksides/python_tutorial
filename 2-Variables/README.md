# Data

Pretty much all programs will deal with some form of data - getting data from the user or other sources,
manipulating it, storing it, displaying it, sending it over the internet - so it's critical for any programmer to
know how their language handles this.

To illustrate, let's consider a program that asks the user their name, and then gives them a personalized greeting such
as `Hello, <name>!`... actually, let's *not* consider it, because we have one right in this directory!

Go ahead and run `Variables.py` in the terminal.  The output should look like this:

```
$ python3 Data.py
Hi!  What's your name? 
```

It's asking you a question!  Go ahead and type your name and press enter.

```
$ python3 Data.py
Hi!  What's your name? Brandon
Hello, Brandon!
```

And that's it!  A simple task, perhaps, but in order to do this, the program has to receive input from the user,
keep track of the data it gets, and refer back to it later to display it on the screen.  To see how this is working,
let's take a look under the hood.  Open Data.py to see what's happening.