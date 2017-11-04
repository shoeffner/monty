% Practical Python


# Built-in functions for your everyday tasks

We already discussed some [built-in
functions](https://docs.python.org/3/library/functions.html), for example:

- `open`: Opens a file
- `str`, `float`, `int`: Casts data to the respective types
- `range`: Generates a sequence of numbers
- `enumerate`: Gives us indices and items for iterations
- `set`, `list`, `tuple`, `dict`: Create the corresponding collections


# Built-in functions

![Built-in Functions. [@pythondocs]](img/builtin_overview.png)


# Built-in functions

![Green: You know these. Orange: Cover these on your own. Red: Today! Blue: Future sessions. Grey: We won't need these. [@pythondocs]](img/builtin_overview_marked.png)


# Homework issues: `__repr__`

```{ .python .exec }
class Car:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.color + ' car'

cars = [Car(c) for c in ('blue', 'red', 'yellow')]
print(cars)
```

::: notes

The print functions tries to call `__str__` for all objects you give it.
Here, the object is a list! The list's `__str__` function calls its elements'
`__repr__` functions.

:::


# Homework issues: `__repr__`

`__repr__` should return a string which can be used to create an object which is similar:

\scriptsize

```{ .python .exec }
class Car:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.color + ' car'

    def __repr__(self):
        return 'Car("' + self.color + '")'

cars = [Car(c) for c in ('blue', 'red', 'yellow')]
print(cars)
```

\normalsize


# Homework issues: x is not `callable`

A variable is callable if it is for example a function:

```{ .python .exec }
number = 5
fun = sum
class Car:
    pass

print('number is callable:', callable(number))
print('fun is callable:', callable(fun))
print('Car is callable:', callable(Car))
```

Why is `Car` callable?

::: notes

`Car` is callable since calling a class (`Car()`) is creating a new instance.

:::

# Homework issues: `*` (tuple unpacking)

```{ .python .exec }
def add(a, b):
    return a + b

print(add(*[1, 2]))
```

`add(*[1, 2])` is equivalent to `add(1, 2)` -- Python "unpacks" the values into
each function argument.


# General questions: `if __name__ == '__main__':`

- Modules have `__name__`s, the one you run `__main__`, others their file or
  directory names (without `.py`).
- `import` executes files
- To avoid random prints etc. on import, "secure" your code in `if` block:
    * `if __name__ == '__main__':`
- For extra karma you can put every code in that block into a function (usually `main`):
    * `def main():`
    * Call `main` inside the `if` block
    * This avoids global scope *pollution*


# Find the lowest number

```{ .python }
vacation_offers = [1023.43, 983.4, 985.12, 1014.52]
```


# Find the lowest number

```{ .python .exec }
vacation_offers = [1023.43, 983.4, 985.12, 1014.52]
low = float('inf')
for offer in vacation_offers:
    if offer < low:
        low = offer
print(low)
```


# Find the highest number

```{ .python .exec }
vacation_offers = [1023.43, 983.4, 985.12, 1014.52]
high = -float('inf')
for offer in vacation_offers:
    if offer > high:
        high = offer
print(high)
```


# Python can do it already!

```{ .python .exec }
vacation_offers = [1023.43, 983.4, 985.12, 1014.52]
print(min(vacation_offers))
print(max(vacation_offers))
```


# Any & All

```{ .python }
none_true = [False, False, False, False]
some_true = [True, False, True, False]
all_true = [True, True, True, True]
```

::: notes

A very common operation is to check if some values fulfill some condition, all
match it, or none.

Later we will see how we can easily create lists of boolean values like the
ones above.

:::


# Any & All

\scriptsize

```{ .python }
none_true = [False, False, False, False]
some_true = [True, False, True, False]
all_true = [True, True, True, True]

def any_true(tocheck):
    for elem in tocheck:
        if elem:
            return True
    return False

def all_true(tocheck):
    for elem in tocheck:
        if not elem:
            return False
    return True

print('Any in none?', any_true(none_true))
print('Any in some?', any_true(some_true))
print('All in some?', all_true(some_true))
print('All in all?', all_true(all_true))
```

\normalsize


# Any & All

```{ .python }
none_true = [False, False, False, False]
some_true = [True, False, True, False]
all_true = [True, True, True, True]

print('Any in none?', any(none_true))
print('Any in some?', any(some_true))
print('All in some?', all(some_true))
print('All in all?', all(all_true))
```


# Sorting in Python

```{ .python .exec }
sorted_list = sorted([9, 2, 5, 3, 1, 8, 19])
print(sorted_list)
sorted_list = sorted([9, 2, 5, 3, 1, 8, 19], reverse=True)
print(sorted_list)
```


# Sorting by key

```{ .python .exec }
def get_age(item):
    return item['age']

unsorted_dicts = [{'age': 23}, {'age': 25}, {'age': 21}]
sorted_dicts = sorted(unsorted_dicts, key=get_age)
print(sorted_dicts)
```

::: notes

If you attempted the difficult bonus exercise last week, you already saw how to
use a key function. Now we will shed some light into it.

:::


# Passing functions around

\scriptsize

```{ .python .exec }
def shout():
    print('HELLO!')

def whisper():
    print('hello...')

def do_something(what):
    what()

do_something(whisper)
do_something(shout)
```

\normalsize

::: notes

Python always passes by *object reference*. For some objects, those which are
mutable, this means that we get references to those objects which we can use
and modify. For others, like integers and strings (which are immutable) they
get copied themselves.

:::


# Mutable objects

```{ .python .exec }
def mutate(some_list):
    some_list.append(1)

my_list = []
mutate(my_list)
mutate(my_list)
print(my_list)
```


# No reassignment possible

```{ .python .exec }
def cantreassign(some_list):
    some_list = [1, 2, 3]

my_list = []
cantreassign(my_list)
print(my_list)
```


# Using function objects: `map` and `filter`

Python has two interesting functions: `map` and `filter`

Both take two arguments: A function, and an iterable (e.g. a list, a string,
...)


# `map`

`map` calls the passed function on each element and stores the results into
a `map` object. This can be transformed into a list:

```{ .python .exec }
def square(x):
    return x * x

in_list = [1, 2, 3, 4, 5]
out_list = list(map(square, in_list))
print(out_list)
```


# `filter`

`filter` calls the passed function on each element and stores those elements,
for which the result is not `False`, into a `filter` object. This can be
transformed into a list.

```{ .python .exec }
def is_even(x):
    return not x & 1

in_list = [1, 2, 3, 4, 5]
out_list = list(filter(is_even, in_list))
print(out_list)
```


# `map` and `filter`

Chaining is possible (even without explicit list conversions in between):

```{ .python .exec }
def is_even(x):
    return not x & 1

def square(x):
    return x * x

in_list = [1, 2, 3, 4, 5]
out_list = list(map(square, filter(is_even, in_list)))
print(out_list)
```


# Using function objects: Comparison to lists

\scriptsize

```{ .python .exec }
def is_even(x): return not x & 1

def square(x): return x * x

in_list = [1, 2, 3, 4, 5]
out_list = list(map(square, filter(is_even, in_list)))
# is equivalent to
acc_list = []
for x in in_list:
    if is_even(x):
        acc_list.append(square(x))

print(out_list)
print(acc_list)
```

\normalsize

::: notes

Don't write functions like this, I just save some space.

:::


# Using function objects: Comparison to list comprehensions

\small

```{ .python .exec }
def is_even(x): return not x & 1

def square(x): return x * x

in_list = [1, 2, 3, 4, 5]
out_list = list(map(square, filter(is_even, in_list)))
# is equivalent to
acc_list = [square(x) for x in in_list if is_even(x)]

print(out_list)
print(acc_list)
```

\normalsize

::: notes

You can read up a little bit more about how to unroll list comprehensions here:
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

Take a look at the for loop inside the for loop for a hint for the homework ;-)

:::


# Nested functions

```{ .python .exec }
def hello():
    hi = 'Hello'
    def world():
        return 'World'
    print(hi + world())

hello()
world()
```

::: notes

Functions are just normal variables, so it's even possible to nest them, i.e.
having function declarations inside of function declarations.

They are only available inside the scope they were declared (except for when
you return them and use them somewhere else).

:::

# Nested functions can access variables

```{ .python .exec }
def times(x0, x1):
    def add(y):
        return y + x1
    result = 0
    for i in range(x0):
        x1 += 1
        result = add(result)
    return result, x1

print(*times(4, 5))
```

::: notes

They can access variables inside the scope they were declared.

In the example, the result is 30 and 9 because:

- `range(4)` has 4 values
- `x1` is incremented in each of the four iterations *before* doing the addition
- `x1` thus takes the values: 6, 7, 8, 9.
- $6 + 7 + 8 + 9 = 30$.

:::


# You can return nested functions

```{ .python .exec }
def create_adder():
    def adder(x, y):
        return x + y
    return adder

my_add = create_adder()
print(my_add(5, 7))
```


# Lambdas

```{ .python .exec }
add = lambda x, y: x + y
print(add(4, 5))

print((lambda x, y: x + y)(9, 3))
```

::: notes

You have seen that it's possible to pass functions around.

This is cool, but sometimes you don't want them to have names and clutter your
scope or you feel like this is not a function worth reusing much.

This is where lambdas come into play: small anonymous functions.

They work like normal functions but are slightly limited:

- They don't have a name
- They can only have one statement (which is automatically the return statement)

:::


# Why nested functions and lambdas?

- Nested functions and lambdas are used as simple functions for e.g. the
  `sorted`'s `key` argument.
- They are often used to be passed around.
- They allow *inline* specification of functions you don't really feel worth to
  be proper functions, e.g. adding two values or combining them into tuples.


# `zip`

One powerful functions is `zip`.

Often you will that you have some data which looks like this:

`[(x0, y0), (x1, y1), (x2, y2)]` or `[(x0, y0, z0), (x1, y1, z1), (x2, y2, z3)]`

Or sometimes it will be separate lists:

`[x0, x1, x2]`, `[y0, y1, y2]`, and `[z0, z1, z2]`.

And of course, your favorite plotting library always takes it the other way.


# `zip`

```{ .python .exec }
x = [1, 3, 5]
y = [2, 4, 6]
c = list(zip(x, y))
print(c)

# reverse
x_n, y_n = zip(*c)
print(list(x_n), list(y_n))
```

::: notes

`zip` works like a zipper. If you have to sides of a zipper `[1, 3, 5]` and
`[2, 4, 6]` it will create pairs of those *tooth* which belong together:
`list(zip([1, 3, 5], [2, 4, 6]))` results in `[(1, 2), (3, 4), (5, 6)]`.

It is generalized to higher dimensions: If you have $n$ lists with $m$
elements, you will get one list with $m$ tuples containing $n$ elements --
always the matching ones. That means the `i`-th element of all $n$ lists will
be inside the `i`-th tuple.

Using tuple unpacking (twice, once to pass the arguments and once implicitly
using the return values) you can reverse the process.

:::


# `zip` in higher dimensions

```{ .python .exec }
x = [1, 4, 7]
y = [2, 5, 8]
z = [3, 6, 9]
c = list(zip(x, y, z))
print(c)

# reverse
x_n, y_n, z_n = zip(*c)
print(list(x_n), list(y_n), list(z_n))
```


# `dir`

The `dir` function is the last built-in function we discuss today.
It allows you to inspect attributes of an object:

\scriptsize

```{ .python .exec }
from textwrap import fill
dir_out = dir('abc')
print(fill(', '.join(dir_out)))
```

\normalsize

::: notes

While this is not really something you use in practice, it allows you to debug
some of your programs or to get some ideas of what might be available for your
objects.

In the example you can see many functions and attributes `str` objects have.

:::


# Your eighth homework

Today we discussed the differences between

* `map`, `filter`, `lambda` (and other functions)
* lists with accumulators
* list comprehensions

- Implement some simple lists using all of the above methods to get an idea of
  how to transform between them and which are more appropriate in which
  situation.
- Use a custom function to sort cars by their comfort.


# References
