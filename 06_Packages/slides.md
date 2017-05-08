% Python Packages


# Homework issues

- Code written by others is always hard to read
- Usually complex code can't be read "from top to bottom"


# Try things out

Download the files accompanying the lecture slides to follow along today.
(Also your homework or our solutions from last week.)


# No `matplotlib`. :-(

Even though it was announced off the record last week: We will not use
`matplotlib` just yet. Sorry for that.

Agenda for today:

- Two algorithms
- Python packages and modules

\note{
Even though it was announced: We will not use `matplotlib` just yet.

Instead I will for the next two weeks or more focus more on programming -- in
Python and in general.

This will, or so I hope, make it much easier for you to use any "library" like
`matplotlib` in the future and make you better programmers even when you don't
use Python for future projects.
}


# Euclid's algorithm

Given two natural numbers, find their greatest common divisor.

# TODO

# TODO: Strassen?

# Organizing code

Or: How to write code that others (and my future me) understand?

- use sufficient documentation and comments  `# covered last week`
- use functions  `# also covered`
- use modules  `# now more of this!`


# Documentation and comments

Open spyder, run one of your files, e.g. the `iris_statistics.py`.

Type `help(functionname)` -- you can now see the documentation of that function.


# Function arguments

The `help` function takes a *function* as an argument. Wait, what? A function?

Try:

```{ .python .exec }
def fun():
    return 'Hello'
hello = fun
print(hello())
```

\note{
- Functions are just *objects* which also have a name, just like variables.
- The difference is that functions are *callable*, that means we can use `function(...)` to execute the code behind it.
}


# Functions as variables

\small

Spyder hides functions (and modules) in its variable explorer, but we can view them by unchecking *Exclude unsupported data types* in the menu.

\normalsize

![Spyder's variable explorer](img/spyder_variables_show_unsupported.png)

\note{
You can call `help` with any of these! Even with modules!


Those without spyder can use this code to check for what is imported:

`store = set(globals().copy()) | set(('store', ))`
`import ...  # whatever we do in the example ;-)`
`print(set(globals()).difference(store))`
}


# Import

```{ .python .exec }
import statistics

help(statistics)
```

\note{
In order to have a function or module available, we need to import it.
}


# Import

Importing a module means to execute everything "global":

- Function definitions are common
- Statements which are not inside a function
- etc.

\note{
This is one of the reasons we can think of function names as variables, as the import just "passes them along".
}


# Python path

\small

We can check our python path, i.e. where python searches for modules:

\scriptsize

```{ .python }
import sys
print(sys.path)
```

```{ .python .hide .exec }
from pprint import pprint as print
import sys
print(sys.path)
```

\normalsize

\note{
We can import from anywhere inside our python path.

Notice the `''` (empty string) as the first element. That's basically "the
current working directory".

Python searches in all of these from the first to the last for modules you try
to import. As soon as it finds a match, that module is imported.

Of course, on your computers it will look different than what you see here.
}


# Writing our own modules

\scriptsize

```{ .python file=06_Packages/code/lecture/reader.py }
```

\normalsize

\note{
This is now a module containing one function.
}


# Using a module

```{ .python wd=06_Packages/code/lecture .exec file=06_Packages/code/lecture/printer.py }

import reader
data = reader.read_data('example.data')
print(data)
```

\note{
Using the `import` statement it is possible to employ functions from another
file.

Notice that we used `import reader` and not `import reader.py`! We are only
interested in the name, not in the type.

To call the function, we need to specify the module name and the function
name: The module name is just the name of the Python file: `module.function()`, here `reader.read_data(...)`.
}


# Reusing a function: directory structure

\scriptsize

```{ .python wd=06_Packages/code/lecture file=06_Packages/code/lecture/printer.py }
```

\normalsize

For this to work, our directory needs to have all files next to each other[^wd]:

\dirtree{%
.1 wd.
.2 reader.py.
.2 printer.py.
.2 example.data.
}

[^wd]: **wd** is the working directory, so where we `cd` to before running the code.


# A more complex directory structure

Consider the following directory tree:

\dirtree{%
.1 wd.
.2 lecture.
.3 reader.py.
.3 printer.py.
.3 example.data.
}

It is possible to `import`:

- `import lecture`. Allows accessing e.g. `lecture.reader.read_data(filename)`.
- `import lecture.reader`. Behaves similar to the above, but excludes the printer.

However, `lecture.printer` does not work! It uses `import reader`.

\note{
Imports are relative to the current directory or to the directories inside the Python path.

A directory can also be a module if it contains proper Python files, just as `lecture` is here.
}


# Import failure

\scriptsize

```{ .python .exec wd=06_Packages/code }
import lecture
import lecture.reader
import lecture.printer
```

\normalsize


# `from ... import ...`

Demo!

\scriptsize

```{ .python wd=06_Packages/code/lecture file=06_Packages/code/lecture/importexamples.py }
```

\normalsize

\note{
We can already see that modules are bundled into meaningful parts.

The `statistics` modules contains, who would have thought, statistics functions.

The `os` module contains a lot of functions handling information from the
operating system (OS). For some parts there is so much (e.g. path handling)
that it even has some submodules (`os.path`).
}


# `if __name__ == '__main__':`

\scriptsize

Consider these files `a.py`, `b.py`, and `c.py` next to each other.
How often will `python a.py` print "Hello World!", and which ones?


```{ .python file=06_Packages/code/lecture/cliqr/a.py }
```

```{ .python file=06_Packages/code/lecture/cliqr/b.py }
```

```{ .python file=06_Packages/code/lecture/cliqr/c.py }
```

\normalsize

\cliqr{Which "Hello World!"s will we see when running `python a.py`?}


# `if __name__ == '__main__':`

```{ .python file=06_Packages/code/lecture/cliqr/a.py wd=06_Packages/code/lecture/cliqr .exec }
```

\note{
Explanation:

- a imports b.
- During b's import, b in turn imports c.
- c declares a function and prints "Hello World! c"
- b, finishing c's import, can now print "Hello World! b"
- a can now import c -- since b already did that, python does not execute c again.
- a prints "Hello World! a"
}


# `if __name__ == '__main__':`

If `b` and `c` were modules written by other programmers, would we expect them to print something during the import?

Most likely not.


# `if __name__ == '__main__':`

Each module gets a magic name. It's accessible via the variable `__name__`.

\scriptsize

```{ .python .exec wd=06_Packages/code/lecture}
import os
import statistics
import reader  # the file we wrote before
print('os name:', os.__name__)
print('statistics name:', statistics.__name__)
print('reader name:', reader.__name__)
print('this name:', __name__)
```

\note{
Notice that the file we execute gets the name `__main__`.

We can use this for a nice trick!
}


# `if __name__ == '__main__':`

\scriptsize

```{ .python file=06_Packages/code/lecture/ifmain/mymath.py }
```

\normalsize

```{ .python wd=06_Packages/code/lecture/ifmain .exec }
import mymath
print(mymath.add(32, 453))
```

\note{
Since the `__name__` variable will be `__main__` for the script we use, we can
put everything which should not be executed into an if-block.
}


# `if __name__ == '__main__':`

\scriptsize

```{ .python file=06_Packages/code/lecture/ifmain/mymath.py .exec }
```

\normalsize


# Packages

\small

A bundle of several modules is usually called a package.

\normalsize

![[pypi.python.org](https://pypi.python.org/pypi) -- the Python package Index](img/pypi.png){ height=150px }

\note{
While there are lots of packages (> 100,000) online available, many of them are very specific.

We will mostly work with the core library, as it already has many cool things.
}


# `__init__.py`

While reading up about packages and modules yourself, you might stumble across the `__init__.py`.

It has mainly two purposes:

- hint for Python: this is a package/module!
- gets executed when the directory is imported
- handles some specifics about the `from ... import *` (defines what `*` actually imports)

\dirtree{%
.1 mypackage.
.2 \textunderscore{}\textunderscore{}init\textunderscore{}\textunderscore{}.py.
.2 mymodule.py.
.2 mysubmodule.
.3 \textunderscore{}\textunderscore{}init\textunderscore{}\textunderscore{}.py.
.3 myothermodule.py.
}


# Your sixth homework

- Perform a matrix multiplication using the divide and conquer algorithm.
- Write a math package which has modules for each, vector and matrix calculations.
- Write your own `help` function.

\dirtree{%
.1 hw6.
.2 ndmath.
.3 vector.py.
.3 matrix.py.
.2 calculator.py.
.2 helper.py.
}


# The last slide

![Parser-tongue Harry [@sawyer2014]](https://pbs.twimg.com/media/ByZVWXgIIAA5Y2D.png)


# References
