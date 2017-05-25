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


# Use cases for exception handling

When writing your own programs, you will mostly have to deal with exceptions when facing user input.

But there are other situations: Reading files, downloading data, program interruptions, ...


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

For the rest of the course, we will focus on applications.


# Your ninth homework


# References
