% Handling Errors and Debugging


# Error messages

```{ .python .exec }
print 'Hello World!'
```


# Reading error messages

```{ .changelog }
  File "<stdin>", line 1
    print 'Hello World!'
                       ^
SyntaxError: Missing parentheses in call to 'print'
```

\note{
- `File "<stdin>", line 1`: Location in file
- `print 'Hello World!'`: Faulty line
- `^`: Where in the line?
- `SyntaxError`: Error type
- `Missing parentheses in call to 'print'`: Description
}



# Longer error messages

```{ .python .exec }
def printer():
    print(x)

def caller():
    printer()

caller()
```

\note{
- For nested calls, a Traceback is returned
- From top to bottom you can figure out what was called.
}


# `SyntaxError`: Missing parentheses

```{ .python .exec }
print 'Hello World!'
```


# `SyntaxError`: Missing parentheses

```{ .python .exec}
print('Hello World!')
```


# `SyntaxError`: Invalid Syntax

```{ .python .exec }
print("What is "Python"?")
```


# `SyntaxError`: Invalid Syntax

```{ .python .exec }
print("What is \"Python\"?")
```


# `SyntaxError`: Unexpected character

```{ .python .exec }
print("Are you" + \" + "Monty" + \" + "?")
```

(Unexpected character after line continuation character)

\note{
The line continuation character is `+`.
}


# `SyntaxError`: Unexpected character

```{ .python .exec }
print("Are you \"Monty\"?")
```


# `SyntaError`: EOF[^eof] while scanning...

```{ .python .exec }
string = "Hello World!
print(string)
```

[^eof]: EOF stands for end of file.


# `SyntaError`: EOF while scanning...

```{ .python .exec }
string = "Hello World!"
print(string)
```


# `SyntaxError`: invalid syntax II

```{ .python .exec }
import turtle
turtle.shape('turtle'=
turtle.forward(100)
turtle.right(90)
```


# `SyntaxError`: invalid syntax II

```{ .python }
import turtle
turtle.shape('turtle')
turtle.forward(100)
turtle.right(90)
```


# Summary `SyntaxError`

`SyntaxError`s occur whenever you type something Python can't decipher.
They are found before the code is actually executed.

Most common causes:

- Missing parentheses
- Missing escape characters or quotes
- Typographical errors


# `TypeError`: object is not callable

```{ .python .exec }
import random
my_random_number = random()
print(my_random_number())
```


# `TypeError`: object is not callable

```{ .python .exec }
import random
my_random_number = random.random()
print(my_random_number())
```


# `TypeError`: object is not callable

```{ .python .exec }
import random
my_random_number = random.random()
print(my_random_number)
```


# `TypeError`: must be X, not Y

```{ .python .exec }
x = 10
print('I have ' + x + ' bottles')
```


# `TypeError`: must be X, not Y

```{ .python .exec }
x = 10
print('I have ' + str(x) + ' bottles')
print('I have', x, 'bottles')
```


# `TypeError`: X is not iterable

```{ .python .exec }
numbers = 5
for x in numbers:
    print(x)
```


# `TypeError`: X is not iterable

```{ .python .exec }
numbers = [5]
for x in numbers:
    print(x)
```


#  Summary `TypeError`

`TypeError`s occur whenever you try something with an object it does not support.

Most common causes:

- Calling a module or variable (i.e. putting parentheses behind it)
- Using a dyadic operator on two different types it does not support
- Using non-iterable types as iterables


# Other errors

There is a [full list of built-in Python
errors](https://docs.python.org/3/library/exceptions.html#concrete-exceptions)
in the documentation.

Some important ones you might encounter:

- `IndexError`: You tried to access the wrong elements in a list
- `KeyError`: A dictionary key is not found
- `ZeroDivisionError`: Don't try `1/0`
- `NameError`/`UnboundLocalError`: Something is not yet defined (in the proper scope)

... and many, many more.


# How to deal with errors?

- Read the error message.
- If you have an idea where it's from, try to fix it.
- Search the web: Search for the exception type, check the documentation, etc.
- If you identified the problem: fix it.
- It happens only in one out of 100 iterations? Great, let's check the debugger!


# Debugging

- A debugger allows to stop code during its execution
- We can inspect variables after each step!


# Interactive Python DeBugger (ipdb)

![Spyder debug controls: Run/Pause, execute next line, step in, step out, run to breakpoint, stop](img/spyder_debug_controls.png)


# Live demo

```{ .python .exec }

```


#

![Spyder debug controls](img/spyder_debug_controls.png)


# Your fifth homework

- We wrote a little script, but it's horribly broken. Try to fix it and add proper documentation.


# The last slide

TODO
