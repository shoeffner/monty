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

\note{
The print functions tries to call `__str__` for all objects you give it.
Here, the object is a list! The list's `__str__` function calls its elements'
`__repr__` functions.
}


# Homework issues: `__repr__`

`__repr__` should return a string which can be used to create an object which is similar:

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


# Homework issues: x is not `callable`

TODO


# Homework issues: `*` (tuple unpacking)

TODO


# General questions: `if __name__ == '__main__':`

TODO


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

\note{
A very common operation is to check if some values fulfill some condition, all
match it, or none.

Later we will see how we can easily create lists of boolean values like the
ones above.
}


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

\note{
If you attempted the difficult bonus exercise last week, you already saw how to
use a key function. Now we will shed some light into it.
}


# Passing functions around

TODO


# List comprehensions, loops, `map` and `filter`

TODO


# zip

TODO


# dir

TODO



# Your eighth homework


# The last slide

![](img/builtin_overview.png)


# References
