% Variables, Assignments, and Functions


# Python scripting

- Scripts make code reusable
- From now on, write all your homework in scripts
- You can still explore using the interactive interpreter

- To replay your code: `python my_code.py` -- or just click the play button in spyder!

\note{
During the first homework, you copied all your commands into files.

You can run them, share them, modify them.
}


# Common mistakes & bonus solutions

- Please name your files as we suggest, if we give you some names.
    `nicolas.py`, `nicholas.docx`, or  `Nicholas.py` are not the same as `nicholas.py`.
- For the bonus questions we needed *escaping*, that means we can write:

```{ .python .exec }
print("This is \"interesting\".")
```

# Some conventions

- No spaces between function names and parentheses, but after commas:
    `function_name(arg0, arg1)`
- Spaces around math operators (we learn more about them today):
    `a * b`
- At least one, better two lines after your `import`s:
    ```{ .python }
    import turtle


    turtle.shape('turtle')
    turtle.done()
    ```
- `import`s should be the first statements in your files.


# Variable vs. value

* Variables are placeholders
* Values are the contents


# Variable vs. value: Random mug

![Mug of Tea (Factorylad, Wikimedia Commons)](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Mug_of_Tea.JPG/1024px-Mug_of_Tea.JPG)


# Variable vs. value: Mensa mug

![Mug of Hot Chocolate (own picture)](mensamug.jpg)


# Example: Liquids

```{ .python .exec }
mug = 'mensa mug'
liquid_in_mug = 'hot chocolate'

print('My', mug, 'contains', liquid_in_mug)
```

\note{
You might know this concept from Logics, Mathematics, or Statistics classes.

A variable is thus just a placeholder for a concept, while the value is its
realization.
}


# Example: Names

```{ .python .exec }
name_one = 'Aline'
name_two = 'Basti'
greeting = 'Good morning,'

print(greeting, name_one)
print(greeting, name_two)
```


# Example: Variable to variable assignment

```{ .python .exec }
my_fruit = 'Raspberry'
your_fruit = my_fruit

print(my_fruit)
print(your_fruit)
```


# Example: Variable to variable assignment

```{ .python .exec }
my_fruit = 'Raspberry'
your_fruit = my_fruit
my_fruit = 'Blueberry'

print(my_fruit)
print(your_fruit)
```

\note{
We can copy over one variable to another variable.

However, be careful with assigning variables to variables, we will later learn
that sometimes we hold the same fruit, not a copy!
}


# Variables and assignments

> A notorious example for a bad idea was the choice of the equal sign to denote
> assignment.[^wirth]

[^wirth]: @wirth2006: Good Ideas, Through the Looking Glass.


# Assignment `=` vs. equality $=$

$a = b$ (in math) is not the same as `a = b` (in code)

\note{
- Mathematical equality works different than assignments
- In maths, both sides of the equality sign have to be equal
- In programming, after "assigning b to a", `a` has the value of `b`
- It does not matter what value `a` or `b` had before (in python)
}


# Variables and math

```python
a = 3
b = 5
c = 2
c = a * b
print(c)
```

\cliqr{What do you expect `c` to be?}


# Variables and math

```{ .python .exec }
a = 3
b = 5
c = 2
c = a * b
print(c)
```


# Math operations

There are lots of math operators:

`+`
  ~ Addition: `5 + 3`

`-`
  ~ Subtraction: `5 - 3`

`*`
  ~ Multiplication: `5 * 3`

`/`
  ~ Division: `5 / 3`

`%`
  ~ Modulo `5 % 3`

\note{
They all work just as we are used from mathematics.

Try out:

- `5 + 3 * 2`
- `(5 + 3) * 2`
- `5 - 2 + 3`
- `5 - (2 + 3)`
- etc.
}


# Recap: modulo

You have 13 apples and want to share between you and your three friends when
you head out for a hike. But since the apples become brown if you slice them,
you only take whole apples with you. How many apples do you leave at home?

\begin{align}
    13& : 4 = 3 R 1 \\
    \underline{12}& \\
     1&
\end{align}


# More math operators

What do these operators do?

`//`
  ~ ?: `5 // 3`

`**`
  ~ ?: `5 ** 3`

\note{
`//` is the integer division (floors the value / cuts off the remainder)

`**` is exponentiation
}

# Python handles very large numbers

Try:

```{ .python .exec .interactive }
>>> 2394 ** 23
>>> 5.331 ** 413
```


# Roots

- Take the square root of 64 ($\sqrt{64}$)[^remindersqrt].
- Take the cube root of 8 ($\sqrt[3]{8}$).

[^remindersqrt]: Remember that $\sqrt[p]{x} = x^{\frac{1}{p}}$.

\note{
\pycode{sqrt_cbrt.py}
}


# Operator precedence and parentheses

- What is $x$: $x = 5 \cdot 4 + 1$
- What is $y$: $y = 5 \cdot (4 + 1)$

\note{
Multiplication has a higher precedence than addition.

Parentheses overwrite precedence.
}


# Operator Precedences

Strength[^strength] Operators              Explanations
------------------- ---------------------- ------------------------------------------
strongest           `(...)`                Parentheses[^parens]
stronger            `**`                   Exponentiation[^exp]
strong              `+x`, `-x`             Positive/Negative numbers
weak                `*`, `/`, `//`, `%`    Multiplication, (Integer) Division, Modulo
weaker              `+`, `-`               Addition, Subtraction
weakest             `=`                    Assignment (not equality!)

[^strength]: Equally strong operators are executed left to right, unless
overwritten with parentheses.
[^exp]: Exception: `**` is weaker than `-x` on its *right hand side* (i.e. in
  the exponent).
[^parens]: Parentheses (and other brackets) are resolved from inner to outer.


# Square roots, again.

```{ .python .exec }
import math

a = 5
sqrt_a = math.sqrt(a)
print(sqrt_a)
```

\cliqr{Do you like video games?}

\note{
- There are lots of useful math functions already implemented in Python.
- Search the web for `python 3 math`. Do it now!
- All functions listed there are available by calling `math.function(...)`
  after `import math`.
- `math` is a **module**

https://docs.python.org/3/library/math.html
}


# Let's solve a "real world" problem!

In the beat 'em up game Castle Crashers, four heroic knights are on an epic
journey to save four princesses who were kidnapped by a dark wizard. During
the knights' journey they fight many evil-doers.

![Castle Crashers, Screenshot [@thebehemoth2012]](http://www.castlecrashers.com/images/screenshots/cc7.jpg){height=200px}


# Fighting for princesses

The knights have different attributes and values assigned to them:

Attribute      Value
-------------- -----
Level ($L$)       31
Strength ($S$)    20

When they hit an enemy with a strong attack, damage $d$ is calculated by
the following formula [@gamefaq2008]:

$d(L, S) = \left\lfloor 5 + 1.15 S + 0.1 L \right\rfloor$

1. Calculate the damage a knight deals with a strong attack.
2. Assume one knight is a bit stronger than the others: with level 32 he got a
   strength value of 21. How much damage does he deal with a single strong attack?

\note{
\pycode{castlecrashers.py}

1. `31`
2. `32`
}


# Fighting for princesses solution

```{ .python .exec file=castlecrashers.py }
```


# Reusing code: Functions

How did you change the code to solve the second exercise?

\note{
Split your code into small parts which solve one task.

- This follows a pattern called DNRY (Do Not Repeat Yourself)
- Fewer mistakes/easy to fix: only need to change them in one place
- We will learn later: It's easier to test
- Makes code reusable
}


# Reusing code: Functions

```{ .python .exec }
def strong_attack_damage(level, strength):
    return (5 + 1.15 * strength + 0.1 * level) // 1

level = 31
strength = 20
damage = strong_attack_damage(level, strength)
print(damage)
```


# Functions -- not yet explained

```{ .python .exec }
def combine(argument, argument1):
    result = argument + argument1
    return result

result1 = combine('Hello', 'World')
result = combine(1, 4)
print(result)
```

\cliqr{What is the value of \texttt{result1}?}

\note{
- `result1` is `HelloWorld`
}


# Functions -- explained

```{ .python .exec }
# "def" is the function keyword
# followed by a name
def combine(argument, argument1):
    # this is the function body: indented!
    result = argument + argument1
    return result  # you can return results

# call it:
result1 = combine('Hello ', 'World')
result = combine(1, 4)
print(result)
```


\note{
- Watch out for indentation
- Take care of enough whitespace around a function (at least one line above and below)
- You can have arbitrarily many arguments
- We will discuss functions in much more details soon,
  but for now this should be sufficient
}


# Your second homework

- Calculate the area of different St. Nicholas' houses. Use the `random`
  module to generate useful random variables.
- Extend the repertoire of the four Castle Crasher knights and let two
  of them fight.


# The last slide

![happy father's day [@climo2014]](http://68.media.tumblr.com/a6e26451c90c25b6fae222c5c0a032d9/tumblr_n76t0oir8H1r5ml59o1_r1_1280.jpg)


# References
