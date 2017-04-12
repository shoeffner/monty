% `True` or `False`?

# How to google mathematical symbols

Remember last week's weird brackets?

$d(L, S) = \left\lfloor 5 + 1.15 S + 0.1 L \right\rfloor$

Whenever you come across a mathematical symbol you do not know Wikipedia's [List of mathematical symbols]( https://en.wikipedia.org/wiki/List_of_mathematical_symbols) might be useful

\note{
Names and explanations of symbols can be looked up, examples included
}

# Another data type: Boolean

There are only two things that can be expressed with the boolean data type:

+ That something is **True**

and

+ that something is **False**

\note{
Nevertheless it is an extremely useful and thus important concept in programming.
}


# Another data type: Boolean

We can *assign* these values to variables. For example:

```python
parrot_alive = True
```

\note{
We assigned the value `True` to the placeholder `parrot_alive`.

Mind the spelling with a capital **T**!
}


# Another data type: Boolean

And we can check whether an expression is *true* or *false*.

```{ .python .exec .interactive }
>>> 5 > 42
>>> 5 < 42
```

We can also check the truth value of previously assigned variables.
```{ .python .exec .interactive }
>>> parrot_alive = True
>>> parrot_alive
```


# Comparison

We can compare numbers using the following operators:

Operator Comparison            `True`         `False`
-------- --------------------- -------------- ---------
`==`     equal                 `1 == 1`       `5 == 3`
`!=`     not equal             `2.3 != 2.313` `5 != 5`
`<`      less than             `2.5 < 9`      `4 < 3`
`>`      greater than          `2.4 > 2.399`  `0.1 > 5`
`<=`     less than or equal    `3 <= 3`       `4 <= 3`
`>=`     greater than or equal `2.4 >= 2.399` `0 >= 5`

\note{
It is possible to compare strings the same way, but it follows less obvious rules.
}


# Chaining

Comparisons can be chained, which is mostly useful for boundary checks:

```{ .python .exec .interactive }
>>> 1 < 2 <= 4 > 3 == 3 != 5
>>> 4 * 8 < 5 * 9 == 45 > 4.2 * 9 < 2
>>> a = 5
>>> 2 < a < 6  # This is a common application
```


# Comparing `True` and `False`

What do you expect from the following three statements?
```python
>>> (1 < 2) < 2
>>> True == 0
>>> False < True
```

\note{
* `True` (`True < 2`)
* `False` (`True == 1`)
* `True`

Careful! `True` is equal to `1`, and `1` only, but for `if` (next slide) every non-zero number is considered `True`!
}


# Using truth values

What does the following code snippet do? What happens when you change the age to 23?

```python
age = 17
if age >= 16:
    print('You may buy beer in Germany.')
if age >= 21:
    print('You may buy beer in the US.')
```


# `if`-statements

`if` is the most basic control flow tool we have.

```{ .python .exec }
c = 4
if c < 5:
    c = 5
print(c)
```


# Intermezzo: indentation

In Python lines of code with the same indentation level are considered a block.

We can not arbitrarily indent our code, but only after certain keywords, like `if`.

```python
if condition:       # if this condition is True
    print('Hello')  # this line will be executed
    print('World')  # and this line as well
print('Good bye')   # this line will ALWAYS be executed
```


\note{
We always indent to the next level with four spaces.
}


# `if` and `else`

Let's take a look at the Collatz conjecture.

\begin{align}
f(x) = \begin{cases}
x / 2  \quad & \text{if } x \text{ is even} \\
3x + 1 \quad & \text{if } x \text{ is odd}
\end{cases}
\end{align}

Let's do it in Python!

\note{
Often `if` is not enough, e.g. in the Collatz conjecture.
}


# Collatz conjecture

```{ .python .exec }
def collatz(x):
    if x % 2 == 0:
        return x // 2
    else:
        return 3 * x + 1

x = 5
y = collatz(x)
print(y)
```


# Collatz conjecture

```{ .python .exec }
def collatz(x):
    if x % 2 == 0:
        return x // 2
    return 3 * x + 1

x = 5
y = collatz(x)
print(y)
```


# What about more cases?

We can also use `elif`, short for `else if`.

```python
age = 23
if age >= 21:
    print('You may buy beer in the US.')
elif age >= 16:
    print('You may buy beer in Germany.')
else:
    print('You may not buy beer.')
```


# Execution order

What is the difference between these three?

------------------ ------------------ ------------------
`age = 23        ` `age = 23        ` `age = 23        `
`if age >= 21:   ` `if age >= 16:   ` `if age >= 16:   `
`    beer = 'US' ` `    beer = 'GER'` `    beer = 'GER'`
`elif age >= 16: ` `elif age >= 21: ` `if age >= 21:   `
`    beer = 'GER'` `    beer = 'US' ` `    beer = 'US' `
`else:           ` `else:           ` `if age >= 0:    `
`    beer = 'No' ` `    beer = 'No' ` `    beer = 'No' `
------------------ ------------------ ------------------

\cliqr{Which one is correct (beer)?}

\note{
The evaluation order matters.

1. correct
2. `beer == 'GER'`, US missing
3. `beer == 'No'`, all get evaluated

Rule of thumb: most constraining conditions first!
}


# Control flow

!['Hey Megan, it's your father. How do I print out a flowchart?' [@xkcd627]](https://imgs.xkcd.com/comics/tech_support_cheat_sheet.png)

\note{
When we talk about control flow we talk about how a program works through data step by step.
}


# How to control flow?

- functions
- `if` statements
- loops


# Loops

```{ .python .exec }
for i in range(10):
    print(i, end=', ')
```

```{ .python .exec }
i = 0
while i < 10:
    print(i, end=', ')
    i = i + 1
```

\note{
Python uses `for` and `while`.

They are mostly exchangeable with a bit of work, but in most cases you will
only need `for`.

`range(stop)` returns a "list" of integers from `0` to `stop`, but excludes
`stop`. For example `range(4)` gives four values: 0, 1, 2, and 3.
}


# `While`

- **while** a condition is true, do something

```{ .python .exec }
counter = 1
while counter <= 5:
    print(counter, end=', ')
    counter = counter + 1
```


\cliqr{What can go wrong?}


# Stopping infinite loops

```{ .python }
while True:
    print('.', end=' ')
```

You can stop program execution with **Control + C**!

\note{
It can very easily happen that you get your conditions wrong or you forget to
change the variable in the condition and your code keeps looping until the end
of time.
}


# `For`

- for each element in this iterable, do something

```{ .python .exec }
for counter in range(6):
    print(counter, end=', ')
```

\note{
Too loop over some collection of values is called "iteration".

Thus, collections of values which allow "iterations" are called "iterables".
}


# `For` and strings

```{ .python }
for item in 'Python':
    print(item, end=', ')
```

\cliqr{What is the output?}


# `For` and strings

```{ .python .exec }
for item in 'Python':
    print(item, end=', ')
```


# Break things...

```{ .python .exec }
counter = 1
while True:
    if counter > 5:
        break
    print(counter, end=', ')
    counter = counter + 1
```

\note{
Break stops the current loop and jumps to the end.
}


# ...Break some more...

```{ .python .exec }
for letter in 'Python':
    counter = 0
    while counter < 5:
        counter = counter + 1
        print(letter, end='')
        if letter == 't':
            break
```

\note{
In this example we only break the inner loop!
}


# ...Then continue

```{ .python .exec }
for item in 'Python':
    if item == 'y':
        continue
    print(item, end=', ')
```

\cliqr{What happens if continue is the last statement in the loop body?}

\note{
Continue skips the remainders of the loop body and jumps back to the top.

If continue is at the end of the loop body, nothing special happens -- the loop would "continue" at this point anyway.
}


# Your third homework

- Learn more about the different control flow operations `if`, `for`, and
  functions by implementing the classic examples "99 bottles" and "Fizz Buzz".
- Draw some beautiful things with the turtle.


# The last slide


# References
