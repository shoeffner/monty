% Errors and Finite State Machines


# Homework issues

TODO


# Handling exceptions

We discussed:

* documentation
* asserts
* debugging

\note{
While most (maybe even all?) errors are called `Error`, you will find me calling them *exceptions*.

Correct would be to call `SyntaxError`s errors and most other errors exceptions.

But since there is no clear distinction between the two, I try to use *exception* on all slides.
}


# Expected exceptions

Sometimes exceptions are expected to happen. Be prepared!

```{ .python }
number = None
while not number:
    value = input('Please enter a number > 0: ')
    number = float(value)
```

What if someone enters a name (and not a number)?


# Try and except exceptions

```{ .python }
number = None
while not number:
    value = input('Please enter a number > 0: ')
    try:
        number = float(value)
    except ValueError as value_error:
        print('Error:', value_error)
```

*Output*:

```{ .changelog }
Please enter a number > 0: Basti
Error: could not convert string to float: 'Basti'
Please enter a number > 0: 0
Please enter a number > 0: 1
```

\note{
`try` runs code until an exception occurs. If that exception was expected, we can catch it with `except`.

Otherwise the program will crash, just as you have seen it many times with exceptions.
}


# Multiple exceptions

Sometimes you want to except multiple exceptions.

There are three ways to do this:

* Excepting all exceptions at once
* Excepting all individually
* A combination thereof


# Excepting multiple exceptions at once

```{ .python }
halogens = {9: 'F', 17: 'Cl',
            35: 'Br', 53: 'I',
            85: 'At'}
number = None
while number not in halogens.keys():
    try:
        number = int(input('Please enter an atomic number: '))
        print('You selected', halogens[number])
    except (ValueError, KeyError) as error:
        print('Sorry!', error)
```


# Excepting multiple exceptions individually

```{ .python }
halogens = {9: 'F', 17: 'Cl',
            35: 'Br', 53: 'I',
            85: 'At'}
number = None
while number not in halogens.keys():
    try:
        number = int(input('Please enter an atomic number: '))
        print('You selected', halogens[number])
    except ValueError as error:
        print('No number', error)
    except KeyError as error:
        print('Key not found', error)
```


# To handle or not to handle?

Which errors should be handled, which ones not?


# To handle

- `KeyError`
- `ValueError`
- `ZeroDivisionError`
- `IndexError`
- and many more


# Not to handle

- `SyntaxError`
- `IndentationError`
- `OutOfMemoryError`
- `RecursionError`
- and many more

\note{
You should never handle exceptions which occur because of the code syntax, nor should you handle exceptions which denote system limitations.

Rule of thumb: Handle only what you can handle with an algorithm.
}


# Finally

\scriptsize

```{ .python .exec }
def read(filename):
    print('Opening')
    handle = open(filename)
    try:
        print('Reading')
        return handle.read().splitlines()
    finally:
        print('Closing')
        handle.close()

read('Makefile')
```

\normalsize

\note{
Statements inside a finally block will always be executed, regardless of
exceptions before or not.

It even works after returns!

It is most commonly used to ensure files and other connections are closed. But
beware: `with` is almost always better!
}


# Finally

\tiny

Exception:
```{ .python .exec }
try:
    a = int('abc')
except ValueError:
    a = -1
finally:
    print('Finally!')
print(a)
```

No exception:
```{ .python .exec }
try:
    a = int('1')
except ValueError:
    a = -1
finally:
    print('Finally!')
print(a)
```

\normalsize


# Raising your own exceptions

\scriptsize

```{ .python .exec }
class CarException(Exception): pass

class Car:
    def __init__(self, broken=False):
        self.broken = broken

    def drive(self):
        if self.broken:
            raise CarException('Broken cars do not drive!')
        print('Driving!')

for car in [Car(), Car(True)]:
    try:
        car.drive()
    except CarException as ce:
        print(ce)
```

\normalsize

\note{
`class CarException(Exception)` means that the class `CarException` *inherits*
all properties the class `Exception` has. We won't discuss inheritance in more
details. But it is important so that you can `raise` exceptions.

The string in the exception you raise should be meaningful: It's the error
message other people will see.
}


# Use cases for exception handling

When writing your own programs, you will mostly have to deal with exceptions when facing user input.

But there are other situations: Reading files, downloading data, program interruptions, ...


# Combining strings and numbers

A common pattern we used so far:

\scriptsize

```{ .python .exec }
wheels = 4
description = 'My car has ' + wheels + ' wheels.'
print(description)
```

```{ .python .exec }
wheels = 4
description = 'My car has ' + str(wheels) + ' wheels.'
print(description)
```

\normalsize


# Format strings

```{ .python .exec }
wheels = 4
description = 'My car has {} wheels.'
print(description.format(wheels))

print('My car has {wheels}.'.format(wheels=6))
```

\note{
The `{}` are delimiters. Here they just serve as placeholders, but we can do
much more with them. Notice the `wheels` in the second case? It allows to name an argument.

Consider: `'I am at ({x}, {y})'.format(y=2, x=5)`.
}


# Format strings are a powerful tool

```{ .python .exec }
print('{:.3}'.format(1/3))
print('{:0>8.3}'.format(4/3))
print('{:*^25}'.format('Hello'))
```

\note{
The `:` means: now comes a format rule!
The format rules then follow a special syntax. The examples here go as follows:

- `.3` Format with 3 decimal places ("After decimal separator, use up to 3 digits").
- `0>8.3` Pad with `0`s (put zeros to fill the width), align right (`>`), make it `8` characters long (at least), and have `3` after the decimal separator. Note that 8 is the *total* length, so there will be $8-3-1$ characters (or more if needed) left of the `.`.
- `*^25` Pad with `*`s, align centered (`^`), make it `25` wide.
}


# Format specifications

![https://docs.python.org/3.6/library/string.html#format-string-syntax](img/stringsyntax.png)

\note{
Now you can create output which looks like you want without having to weirdly concatenate strings and check spaces, etc.

There is much more inside the documentation, we will take a look at some of it now.
}


# Paradigm shift

We have now learned a huge set of tools in Python:

\small

Variables, functions, classes, numbers, strings, error handling, documentation,
lists, dictionaries, sets, tuples, some built-in functions, lambdas, list
comprehensions, mathematical operations, directory structures, imports, naming
and code conventions, input and output, loops, if and else, ...

\normalsize

If you want to go into more details about all those things, I recommend the
[Python Tutorial](https://docs.python.org/3/tutorial/). It covers what we did
and sometimes a little bit more.

For the rest of the course, we will mostly focus on applications.


# Your ninth homework


# References
