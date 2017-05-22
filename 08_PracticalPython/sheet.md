% Exercise Sheet 08 -- Practical Python

# Submission

By the end of this sheet you will have a number of different files to submit.
In Stud.IP you will have a directory for your own group, please upload them
there. It is easier for you if you just archive (preferably zip) all files and
upload your archive, but it is okay if you upload them one by one.


# Exercise 1: There's always more than one way to solve a problem!

Can you write code which performs the following tasks by using a) for loops
with accumulators, b) lambdas (or functions which don't use loops), map and
filter, c) list comprehensions?

- Create a list which contains all pair-wise permutations of the numbers 1, 2,
  and 3. `[(1, 1), (1, 2), (1, 3), (2, 1), ..., (3, 3)]`.
- Create a list which contains all numbers except for those divisible by 3 or
  5, up to 100. `[1, 2, 4, 7, 8, 11, ..., 98]`.
- Create a list which contains the sums of all pair-wise permutations of 1, 2,
  and 3. `[2, 3, 4, 3, ..., 9]`.

Name your file `manyways.py`.


# Exercise 2: Calculator

This week you learned that we can pass around functions to call them. You can
also store them in a dictionary:

```{ .python }
my_functions = {
    'add': lambda x, y: x + y,
}
```

## Simple calculator

Write a little calculator (`calculator.py`) which takes user input (use the
`input` function) in the following forms and prints the correct results:

```{ .changelog }
5 + 87
103 * 32
7 / 3
932 - 472
```

Use a dictionary to select the proper arithmetic method. You can assume all
inputs are properly defined.

Use asserts to check if your calculator returns the correct results.

Add sufficient documentation.


## More complex calculator

**Copy** your simple calculator to `complex_calculator.py`. Extend the complex
calculator to handle parenthesis:

```{ .changelog }
(5 + 3) * 2
6 - (5 + 2)
(3 - 2) * ((4 + (3 - 2) * 3) - 3)
```

You can assume that all inputs are properly defined and don't need to handle
errors.

Add some more asserts and if necessary documentation.
