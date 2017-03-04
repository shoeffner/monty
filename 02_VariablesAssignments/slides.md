% Variables and Assignments


# Variable vs. Value

* Variables are containers
* Values are the contents


# Variable vs. Value

TODO: nice picture of a container with a value, e.g. a coffee mug to fill with coffee or tee


# Example: Liquids

```python
cup = 'coffee'
print(cup)

cup = 'tea'
print(cup)
```


# Example: Names

```python
name_one = 'Aline'
name_two = 'Basti'
greeting = 'Good morning, '

print(greeting, name_one)
print(greeting, name_two)
```


# Example: Variable to Variable assignment

```python
my_fruit = 'Raspberry'
your_fruit = my_fruit

print(your_fruit)
# What about mine?
print(my_fruit)

my_fruit = 'Blueberry'
print(my_fruit)
print(your_fruit)
```

\note{
We can copy over one variable to another variable.

However, be careful with assigning variables to variables, we will later learn
that sometimes we hold the same fruit, not a copy!
}


# Variables and Assignments

> A notorious example for a bad idea was the choice of the equal sign to denote
> assignment.[^wirth]

[^wirth]: Niklaus Wirth: Good Ideas, Through the Looking Glass. 2005


# Assignment `=` vs. Equality $=$

$a = b$ is not the same as `a = b`

\note{
- Mathematical equality works different than assignments
- In maths, both sides of the equality sign have to be equal
- In programming, after "assigning b to a", `a` has the value of `b`
- It does not matter what value `a` or `b` had before (in python)
}


# Variables and Math

```python
a = 3
b = 5
c = 2
c = a * b
print(c)
```

\note{
What do you expect `c` to be?
}


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

```python
2394 ** 23
5.331 ** 413
```


# Roots

- Take the square root of 64 ($\sqrt{64}$)[^remindersqrt].
- Take the cube root of 8 ($\sqrt[3]{8}$).

[^remindersqrt]: Remember that $\sqrt[p]{x} = x^{\frac{1}{p}}$.

# Roots

\note{
`x = 64`

`sqrt_x = x ** (1 / 2)`

`print(sqrt_x)`

`y = 8`

`cbrt_y = y ** (1 / 3)`

`print(cbrt_y)`
}


# Operator Precedence and Parentheses

- Solve for $x$: $x = 5 \cdot 4 + 1$
- Solve for $y$: $y = 5 \cdot (4 + 1)$

\note{
Multiplication has a higher precedence than addition.

Parentheses overwrite precendences.
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
[^parens]: Parentheses (and other brackets) are resolved from innner to outer.


# Square roots, again.

```python
import math

a = 5
sqrt_a = math.sqrt(a)
```

\note{
- There are lots of useful math functions already implemented in Python.
- Google for [`python 3 math`](https://docs.python.org/3/library/math.html). Do
  it now!
- All functions listed there are available by calling `math.function(...)`
  after `import math`.
}


# Let's solve a real world problem!

TODO

\note{
\begin{align}
x = \text{TODO}
\end{align}
}


# Your second homework

TODO


# The last slide

![TODO](http://www.smbc-comics.com/comic/the-dimension-store)

