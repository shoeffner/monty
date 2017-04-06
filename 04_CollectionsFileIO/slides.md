% Collections and File I/O


# Function Arguments -- Positional

```{ .python .exec }
def function(arg0, arg1='default'):
    print(arg0, arg1)

function(0, 1)
function(0)
function(arg1=1, arg0=0)
```

\note{
- Positional arguments are the "normal" way we already discussed to provide variables.
- They always go first, followed by positional arguments with default values.
- A default value is always used if no other value is provided.
- It is possible to use arguments by their names -- the order does not matter.
}


# Function Arguments -- Arbitrary Argument Lists

```{ .python .exec }
def function(*args):
    print(args)

function(1, 2, 3)
```

\cliqr{Can we have multiple argument lists?}

\note{
- Argument lists can not be used by their names.
- Their can only be one argument list, as it would otherwise be
  indistinguishable to which argument list each argument belongs.
- The notation `(1, 2, 3)` is new, we will come back to it in a few slides.
}


# Function Arguments -- Keyword arguments

```{ .python .exec }
def function(**kwargs):
    print(kwargs)

function(arg0=0, mug='tea cup', animal='platypus')
```

\note{
- Keyword arguments can be captured using the double asterisk notation.
- They are stored in a dictionary.
}



# Tuples, Lists, Dictionaries, Sets

Python offers four basic collection types:

- Tuples: `(1, 2, 'hello', 2.3)`
- Lists: `[1, 2, 'hello', 2.4]`
- Dictionaries: `{'a': 1, 'b': 2}`
- Sets: `{1, 2, 'hello'}`


\note{
They are all iterables.

Remember: Strings are iterables as well.
}


# Tuples

```{ .python .exec }
my_fruits = ('apple', 'pear', 'banana')
print(my_fruits)
```

\note{
Tuples are immutable, that means they are copied when we assign them to another
variable.

Tuples are sorted the way they are created.
}


# Tuple functions: `len`

```{ .python .exec }
my_fruits = ('apple', 'pear', 'banana')
print(len(my_fruits))
```


# Tuple functions: indexing

```{ .python .exec }
my_fruits = ('apple', 'pear', 'banana')
print(my_fruits[1])

for i in range(len(my_fruits)):
    print(my_fruits[i], end=' ')
```


# Tuple functions: `index`

```{ .python .exec }
my_fruits = ('apple', 'pear', 'banana')
print(my_fruits.index('pear'))
```


# Tuple functions: merging

```{ .python .exec }
my_fruits = ('apple', 'pear', 'banana')
my_fruits = my_fruits + ('strawberry', )
print(my_fruits)
```

\note{
We can check the documentation or `help(tuple)` for more information about functions.
}


# Lists

```{ .python .exec }
my_fruits = ['apple', 'pear', 'banana']
print(my_fruits)
```


# Lists are slightly different than tuples

```{ .python .exec }
my_fruits = ['apple', 'pear', 'banana']
your_fruits = my_fruits
your_fruits.append('strawberry')
print(my_fruits)
print(your_fruits)
```

\note{
Lists are mutable, which means that we only assign a reference to the object to
our variables -- references both point to the same instance. Thus, we modify
both unless we explicitly "copy" the list.

They are also stored sorted.
}


# List functions: `insert`

```{ .python .exec }
fruits = ['apple', 'pear', 'banana']
fruits.insert(1, 'avocado')
print(fruits)
```


# List functions: `remove`

```{ .python .exec }
fruits = ['apple', 'pear', 'banana']
fruits.remove('pear')
print(fruits)
```


# List functions: `pop`

```{ .python .exec }
fruits = ['apple', 'pear', 'banana']
last = fruits.pop()
print(fruits, last)
```

\note{
It also supports the same as tuples: `len(my_fruits)`,
`my_fruits.index('pear')`, and `my_fruits + ['strawberry']`, indexing, etc.
}


# Dictionaries

```{ .python .exec }
my_foods = {'fruit': 'apple', 'vegetable': 'carrot'}
print(my_foods)
```

\note{
Dictionaries are also mutable.

In general they are stored in the order they are created but it is not
guaranteed, so don't rely on it!
}


# Dictionary functions: `keys` and `values`

```{ .python .exec }
my_foods = {'fruit': 'apple', 'vegetable': 'carrot'}
print(my_foods.keys())
print(my_foods.values())
print(my_foods.items())
```


# Dictionary functions: indexing

```{ .python .exec }
my_foods = {'fruit': 'apple', 'vegetable': 'carrot'}
print(my_foods['fruit'])
```


# Dictionary functions: Adding values

```{ .python .exec }
my_foods = {'fruit': 'apple', 'vegetable': 'carrot'}
my_foods['soup'] = 'potato'
print(my_foods)
```


# Dictionary functions: `pop`

```{ .python .exec }
my_foods = {'fruit': 'apple', 'vegetable': 'carrot'}
my_foods.pop('fruit')
print(my_foods)
```


# Sets

```{ .python .exec }
my_meals = {'lunch', 'dinner', 'dinner'}
print(my_meals)
```

\note{
Sets are unordered and have unique values. They also support some set
operations. However, they are not that often used, although they are quite
useful!
}


# Set operations

```{ .python .exec }
food_a = {'steak', 'apple', 'cauliflower', 'broccoli'}
food_b = {'broccoli', 'cauliflower', 'bell pepper'}
print(food_a & food_b)
print(food_a | food_b)
print(food_a.difference(food_b))
```


# Iteration over Tuples, Lists, and Sets

```{ .python .exec }
fruits = ['apple', 'pear', 'banana']
for fruit in fruits:
    print(fruit, end=', ')
```

\note{
It works exactly the same way for tuples and sets.
}


# Iteration over Tuples, Lists, and Sets with Subscription

```{ .python .exec }
fruits = ['apple', 'pear', 'banana']
for fruit in fruits[1:]:
    print(fruit, end=', ')
```



# Iteration over Dictionaries

```{ .python .exec }
food = {'start': 'soup', 'main': 'pizza',
        'dessert': 'ice cream'}
for key in food.keys():
    print(key, end=', ')
```


# Iteration over Dictionaries -- with values

```{ .python .exec }
food = {'start': 'soup', 'main': 'pizza',
        'dessert': 'ice cream'}
for key, value in food.items():
    print(key, value, end=', ', sep=':')
```

\note{
For dictionaries we have to define what we want to iterate over.
}


# Nested collections

```{ .python .exec }
menu = {'main': ['pizza', 'pasta'],
        'dessert': [
            {'ice cream': ['chocolate', 'vanilla']},
            'mousse au chocolat'
        ]
       }
print(menu['dessert'][1])
```

# Function Arguments and Collections

Write a function `calculator`. It takes a list of arguments and performs the operation provided with the keyword `operation` on all numbers to return one result. Implement it for the operations `+`, `-`, `*`, `/`. If no operation is provided, return the first number.

Example inputs                                   Result
------------------------------------------------ ------
`calculator(1, 2, 3, operation='+')`             6
`calculator(2, 4, 8, operation='*')`             64
`calculator(3, 2, operation='-')`                1
`calculator(1, 2, 3, 4, 5, 6, 7, operation='+')` 28
`calculator(4, 2, 7)`                            4


# Function Arguments and Collections - Solution

```{ .python .exec }
def calculator(*args, **kwargs):
    result = args[0]
    if 'operation' in kwargs.keys():
        for arg in args[1:]:
            if kwargs['operation'] == '+':
                result = result + arg
            # etc.
    return result
print(calculator(1, 2, 3, operation='+'))
```


# I/O

IO or I/O or similar abbreviations usually stand for:

Input and Output

\note{
Handled by (data) streams.

We already used one: the standard output stream ("stdout")
}


# Standard Output Stream

```python
print(*objects, sep=' ', end='\n',
      file=sys.stdout, flush=False)
```

> Print `objects` to the text stream `file`, separated by `sep` and followed by
> `end`. `sep`, `end` and `file`, if present, must be given as keyword arguments.

[Python Documentation, @pythondocs, https://docs.python.org/3/library/functions.html#print]

\note{
- You can ignore the `flush` parameter: some streams first collect data (buffering) and then write it (flush).
- We will now try another stream for `file` -- the default is `sys.stdout`, which means to just print it to the terminal.
}


# `print` to file

```{ .python .exec }
my_lottery_numbers = [21, 8, 19, 9, 1, 22]
with open('04_CollectionsFileIO/code/lottery.txt', \
          'w') as lottery_file:
    print(my_lottery_numbers, file=lottery_file)
```

```{ file=lottery.txt }
```

\note{
File names: try to use relative file names so that everyone can use your code.

File modes: the letter after the file name is the mode. It can be one of:

* `w`rite (overwrites/creates)
- `r`ead (read-only)
- `a`ppend (updates/creates)
- add `+` to open for read and write (e.g. `r+`)
- and some more
}


# read/write to/from file

```{ .python .exec }
my_lottery_numbers = [21, 8, 19, 9, 1, 22]
with open('04_CollectionsFileIO/code/lottery.txt', \
          'w+') as lottery_file:
    lottery_file.write(my_lottery_numbers)
    result = lottery_file.read()
print(result)
```

\note{
You might find other sources on the internet using different notations, e.g.
with "open" and "close" for files -- just use `with` unless you can't. Because
`with` opens the file and automatically closes it for you!

Closing files is important because sometimes other processes are not allowed to
access "used" files, even if you don't really use them anymore.
}


# Cast to the rescue

```{ .python .exec }
my_lottery_numbers = [21, 8, 19, 9, 1, 22]
with open('04_CollectionsFileIO/code/lottery.txt', \
          'w+') as lottery_file:
    lottery_file.write(str(my_lottery_numbers))
    result = lottery_file.read()
print(result)
```


# Seeking the beginning

```{ .python .exec }
my_lottery_numbers = [21, 8, 19, 9, 1, 22]
with open('04_CollectionsFileIO/code/lottery.txt', \
          'w+') as lottery_file:
    lottery_file.write(str(my_lottery_numbers))
    lottery_file.seek(0)
    result = lottery_file.read()
print(result)
print(type(result))
```


# Reconstructing the list properly

```{ .python .exec }
with open('04_CollectionsFileIO/code/lottery.txt', \
          'r') as lottery_file:
    lottery_raw = lottery_file.read()
# This is black python magic! Let's discuss it
numbers = [int(num) for num in \
           lottery_raw[1:-1].split(',')]
print(numbers)
print(type(numbers))
```


\note{
`[int(num) for num in \ `

&nbsp;&nbsp;`lottery_raw[1:-1].split(',')]`

is equivalent to (but shorter to write)

`lottery_no_brackets = lottery_raw[1:-1]`

`lottery_strings = lottery_no_brackets.split(',')`

`lottery_numbers = []`

`for num in lottery_strings:`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`lottery_numbers.append(int(num))`

}

# Using JSON to write

[JSON](http://json.org) (JavaScript Object Notation) is a standard to exchange data. Python understands it.

```{ .python .exec }
import json

my_lottery_numbers = [21, 8, 19, 9, 1, 22]
with open('04_CollectionsFileIO/code/lottery.json', \
          'w') as file:
    json.dump(my_lottery_numbers, file)
```


# Using JSON to read

```{ .python .exec }
import json

with open('04_CollectionsFileIO/code/lottery.json', \
          'r') as file:
    result = json.load(file)
print(result)
print(type(result))
```

\note{
JSON allows us to store much more "complex" data, you will have to deal with
that in the homework.
}


# Your fourth homework




# The last slide

TODO


# References
