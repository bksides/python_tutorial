# Using your Terminal

Many programming tutorials assume that the reader already knows how to use their terminal - a bizarre assumption, given
that most computer users never touch their system's terminal, and almost no one who has never written code will ever
have a reason to open it.

Terminals are text-based programs that allow you to directly issue commands to your computer.  In the early days of
computing, this was the only way to interact with a computer; visual desktops were unheard of.  Python, like most
programming tools, is still used from the terminal, so you will need a passing familiarity with it in order to proceed.
Luckily, while interacting with terminals *can* be very complex, it is very easy to acquire the basics.  The difficulty
lies in the fact that different terminals use different sets of commands, which makes writing a single universal
crash-course challenging.  I will be focusing on two main terminal "dialects": **bash**, which is usually the default
on Linux and Max systems; and **Command Prompt**, used by the default Windows terminal.

## First Glance

When you open your terminal, you will usually see two important things:

1. the Current Working Directory

This is important to keep track of - it tells you "where you are" in the file system.  Anything you do will be done in
the context of this directory.  When you first open your terminal, your CWD should be some "home" directory; on Mac and
some other Unix-like systems, it might be listed simply as `~`.  This tilde is shorthand for your home directory.  On
these systems, you can see the full path of the home directory by typing `pwd` into the terminal and pressing
`Enter`.

2. The Cursor

The flashing cursor is where you type your commands.  Go figure!  Unlike the cursor in most visual programs, the
cursor in most terminals can't be controlled by the mouse.  You can use the `left` and `right` arrow keys to move the
cursor around within whatever text you've typed, and you can usually use the `up` arrow key to repeat the last command
you entered.

## Navigation

The most important set of commands in any terminal are its navigation commands.  If you'd like, feel free to open your
own terminal and follow along with the examples to see what they do.  Lines in the examples beginning with a file path
followed by a `$` are commands you can type in; this is only to distinguish these lines from output lines, which are not
prefixed with this symbol.  You do not need to type the `$` as part of the commands.

Here are some core navigational commands:

- `pwd`: This will print the full path of your current directory.  This is useful for getting your bearings if you
forget where you are in the filesystem.  The Command Prompt equivalent is `echo %cd%`

Example:
```
~$ pwd
/Users/my_username
```

- `ls`: This is used to list the contents of the current directory.  Useful for checking what files and subdirectories
are present.  The Command Prompt equivalent is `dir`

Example:
```
~$ pwd
/Users/my_username
~$ ls
Applications
Desktop
Documents
Downloads
```

- `cd`: This is used to change the current directory.  You can use it to "move" around the file system.  This command
is the same in bash as in Command Prompt.  `cd ..` will move you up one directory in the hierarchy; in bash
environments, `cd ~` will move you to your home directory.

Example:
```
~$ pwd
/Users/my_username
~$ ls
Applications
Desktop
Documents
Downloads
~$ cd Documents
~/Documents$ pwd
/Users/my_username/Documents
~/Documents$ ls
document.txt
otherdocument.txt
thirddocument.txt
~/Documents$ cd ..
~$ pwd
/Users/my_username
```

## File System Manipulation

The next most common task a terminal is used for is file manipulation.  You can create, delete, edit, and move files
and directories straight from the terminal.  This can be more convenient than using a file browser, especially if you
already have a terminal open in the directory you want to modify.  Here are some core file manipulation commands:

- `mkdir`: This command creates a new directory with the given name.  This command is the same in bash as it is in
Command Prompt.

Example:
```
~$ ls
Applications
Desktop
Documents
Downloads
~$ mkdir new_directory
~$ ls
Applications
Desktop
Documents
Downloads
new_directory
~$ cd new_directory
~/new_directory$ pwd
/Users/my_username/new_directory
```

- `rm`: This command deletes a file or directory.  **Files removed with rm are permenantly deleted**; unlike deleting a
file through your file browser, `rm` will not put your file in a "trash" folder, but will simply remove it from the file
system altogether.  In Command Prompt, the equivalent commands are `del` for files and `rmdir` for directories.

Example:
```
~$ ls
Applications
Desktop
Documents
Downloads
new_directory
~$ rm new_directory
~$ ls
Applications
Desktop
Documents
Downloads
```

- `mv`: This command can be used to move a file or directory from one location to another, or to rename a file or
directory.  The equivalent command in Command Prompt is `move`.

Example:
```
~$ ls
Applications
Desktop
Documents
Downloads
my_file.txt
~$ mv my_file.txt new_name.txt
~$ ls
Applications
Desktop
Documents
Downloads
new_name.txt
~$ mv new_name.txt Documents
~$ cd Documents
~$ ls
new_name.txt
```

- `cat`: More of an *inspection* command than a *manipulation* command.  This is used to print the contents of a file
to the terminal.  The Command Prompt equivalent is `type`.

Example:
```
~$ ls
Applications
Desktop
Documents
Downloads
my_file.txt
~$ cat my_file.txt
This is the contents of the file!  Woohoo
```

## Running Programs from the Terminal

The terminal can be used to run programs.  This includes the Python Interpreter; you will use this functionality when
you write python code and run it from the terminal.  You can do this simply by typing the name of the program, possibly
followed by some **arguments** which will be passed into the program for it to interpret.  For example, the `echo`
program simply outputs whatever arguments you give it:

```
~$ echo Hello world!
Hello world!
```

When you type this, your terminal looks through a few system directories where it expects to find your programs.  Once
it finds one called "echo", it runs that program and gives it the rest of the arguments you provided: `"Hello"` and
`"world!"`.

In some cases, the program you want to run will not be located in one of the standard directories, in which case you
will have to provide the full path to the program.  For instance, say you have a program called `myecho` in your
home directory, `/Users/my_username`.  This program simply emulates the behavior of the built-in `echo` program.
Since your home directory is not one of the standard directories, you must provide the full path to this program:

```
~$ /Users/my_username/myecho some random arguments
some random arguments
```

Alternatively, since the program is located in your home directory, you can use the `~` shorthand in place of the full
path:

```
~$ ~/myecho hello world!
hello world!
```

As yet another alternative, one can use a period `.` to refer to the current directory as a shorthand:

```
~$ ./myecho hello world!
hello world!
```