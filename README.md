# Python Tutorial

This is a Python tutorial, complete with runnable examples!  It is intended for complete programming novices.

## Setup

Before you can start following along to this tutorial, you will need to do some setup.  You'll only need two things to
get started, but I'm going to recommend four:

1. A Terminal - You need this!

A **terminal** is a text-based interface for issuing commands to your computer.  Pretty much all computers will have one
of these already.  Opening your terminal can be a different process depending on your operating system, but in most
cases just searching for a program called "terminal" ("cmd" or "command prompt" in Windows) will find you the program
you're looking for.  For more on using the terminal, see exercise [0](/0-Terminal).

2. The Python 3 Interpreter - You need this, too!

Python is a **scripting language**; that's programmer parlance for a language whose programs don't run by themselves.
They require an additional program, called an **interpreter**, which reads the program and *interprets* the instructions
on the fly.  Many computers will have a Python Interpreter installed by default.  You can find out if you have it by
opening your **terminal** and typing `python3 --version` + `Enter`.  If you get an output that looks like this:

```
$ python3 --version
Python 3.X.X
```

You're good to go!  If your terminal tells you the command could not be found, you will
need to install the [Python 3 Interpreter](https://www.python.org/downloads/).

A note on Python versions: Python 3 is the latest version of Python, but many computers still use Python 2 by default.
Since Python 2 is no longer officially supported by Python's maintainers, it's important that new programmers learn to
use Python 3.  If your computer has a Python 2 interpreter installed by default (i.e. if you can run
`python --version` or `python2 --version` and get an output that looks like `Python 2.X.X`), your computer can run
Python 2 programs - but it is nonetheless highly recommended that you install a Python 3 interpreter.  The programs
in this tutorial assume a Python 3 environment.

3. A Decent Text Editor - You should probably have this.

While it is technically possible to create Python programs in any old text editor like Notepad or TextEdit, it becomes
much easier to do so using some specialized editors.  My personal recommendation is
[Microsoft's Visual Studio Code](https://code.visualstudio.com/).  This editor provides syntax highlighting that will
help you make sense of your code, error highlighting to help you fix problems, and has a simple enough interface to
avoid overwhelming you with all the features you might find in more complex editors.  If a slightly more complex
interface doesn't scare you, you might also consider [Github's Atom](https://atom.io/).

4. Git - Get this if you want it.

[Git](https://git-scm.com/) is a tool that makes it easy to move code on and off of sites like Github.  You can use it to download all the code
from this tutorial straight to your computer so you can edit and run it yourself.  Alternatively, you can manually type
the code yourself or copy and paste it into your editor.

If you decide to download Git, you can download everything in this tutorial to your computer using your terminal.  Just
`cd` into a directory where you don't mind keeping some code, and run 
`git clone https://github.com/bksides/python_tutorial`.  This will create a new directory called `python_tutorial`; `cd`
into this directory, and you will see that the entire contents of this tutorial has now been cloned onto your computer!

## Get Coding!

Once you've done all your setup and feel comfortable using your terminal and your text editor, go ahead and
[write your first program!](/1-HelloWorld)