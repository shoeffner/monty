% `True` or `False`?


# Another Data Type: Boolean

There are only two things that can be expressed with the boolean data type:

+ That something is **True**

and

+ that something is **False**

\note{
Nevertheless it is an extremely useful and thus important concept in programming.
}


# Another Data Type: Boolean

We can *assign* these values to variables. For example:

```python
parrot_alive = True
```

\note{
We assigned the value `True` to the placeholder `parrot_alive`.

Mind the spelling with a capital **T**!
}


# Another Data Type: Boolean

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


# Using Truth Values

What does the following code snippet do? What happens when you change the age to 23?

```python
age = 17
if age >= 16:
    print('You may buy beer in Germany.')
if age >= 21:
    print('You may buy beer in the US.')
```


# `if`-Statements

`if` is the most basic control flow tool we have.

```{ .python .exec }
c = 4
if c < 5:
    c = 5
print(c)
```


# Intermezzo: Indentation

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
x = 5
if x % 2 == 0:
    y = x / 2
else:
    y = 3 * x + 1
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

\note{
The evaluation order matters.

1. correct
2. `beer == 'GER'`, US missing
3. `beer == 'No'`, all get evaluated

Rule of thumb: most constraining conditions first!
}


# Your third homework


# The last slide


# References
