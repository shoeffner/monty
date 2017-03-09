% `print('Hello Python!')`

# Programming is easy

But it takes a lot of time to become good at it.

\note{
- It's like sports: easy to run, but it takes a lot of practice to run a marathon.

- You need ten thousands of hours to master a skill -- we can only present you with your first 50 or so.
}


# Why programming?

## Programming in academia

\note{
- Course work focuses more on contents, less on tools
- Data analysis becomes more fluent
- Theses and papers become easier
- You learn to automate things to be more productive
}

## Programming outside of academia

\note{
- Understanding the principles helps with every day tasks:
    - using office programs
    - filing your tax returns
    - understanding insurance policies
    - ...
- Understanding technology makes things easier and less magic
- Basically every single job for academic people involves code
}


# Questionnaire results

[Responses](https://goo.gl/VhpXY1)


# Lecture

- Time: Wednesday, 14:00 - 16:00, c.t.
- Room: 93/E15

(Complete list in Stud.IP)


# Homework

- One sheet per week
- Deadline is before Monday morning, 08:00
- In groups of $\approx \frac{N}{12}$ students (we prefer $2$--$3$)
- Sign up on Stud.IP


# Feedback sessions

- Once per week
- Homework will be checked and commented on
- Not a bad thing, but an opportunity!


# Grading

- Only Fail/Pass
- To Pass: TODO


# Let's learn together

## Ask questions
- Ask questions in class
- Ask questions in the [forum](https://studip.uos.de/plugins.php/coreforum/index/index?cid=e7eca86bfdacf12717540d75bb2fcb47)
- Ask questions per mail

## Share your knowledge
- Collect your error messages and the code which produces them here: TODO
- Try to solve them
- We will have a session soon where we discuss different errors


# Let's program!

We will very often see Pseudocode: algorithms written down in a concise way, but
close to natural language.


# Pseudocode example

```
If it is sunny
    I like to go swimming
If it is rainy
    I like to play in puddles
Otherwise
    I stay at home
```


# Pseudocode example

```
For 10 apples inside the crate:
    Take it out
    Put it into your shopping cart
Move your shopping cart to the cash point
Start a receipt with 0 EUR
For each apple inside your shopping cart:
    Take it out
    Weigh it
    Get the price for the weight
    Increase the receipt with its price
    Put it into your shopping bag
Pay the sum on your receipt
```


# Pseudocode example

Write a little pseudocode yourself! For example:

* How to pass this class?
* What to wear? Red or blue T-shirt?
* ... ?


# Hello World!

The starting program for almost every programming language is a
`Hello World!` program.
It is a program which somehow prints[^print] a friendly message:

```
Hello World!
```

[^print]: "printing" means to output something, usually on the terminal. Don't
  bring out your printers and throw stacks of paper at us. We have nothing to
  throw back.


# Hello World Pseudocode

```
print "Hello World!"
```


# Hello World in Python

```python
print("Hello World!")
```


# Hello World in other programming languages

## MATLAB

```matlab
disp('Hello World!')
```

## Prolog

```prolog
message('Hello World!').
```


# Hello World in other programming languages

## Java

```java
class Main {
    public static void main(String... args) {
        System.out.println("Hello World!");
    }
}
```

## C++

```cpp
#include <iostream>
int main()
{
    std::cout << "Hello World!" << std::endl;
}
```


# Hello World in other programming languages

## Arnold.C

```
IT'S SHOWTIME
TALK TO THE HAND "Hello World!"
YOU HAVE BEEN TERMINATED
```

## Brainfuck

```
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++
..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.
```


# Hello World!

`Hello World!` programs give us a first impression of the language of a syntax.
There are other demo programs but we will take a look into some later.

Keep in mind: the concepts are always very very similar!


# Your first homework

Setup your laptop to run Python (we will discuss this in a minute).
Write your own `Hello World!` program.
Draw a little St. Nicholas' house. (Not on paper, of course.)


# Installing Python

Miniconda is a package management system which allows us to keep the
administrative overhead of installing Python to a minimum.

- Download Miniconda (Python 3.6) from
  [https://conda.io/miniconda.html](https://conda.io/miniconda.html).
- Install it. Make sure it is in your path.
- Open your terminal / command line and run the following to install an
  IDE[^IDE] we will and two packages we might use:
    ```shell
    conda -y install spyder numpy matplotlib
    ```
- For stuff used in e.g. Neuroinformatics, Machine Learning, Computer Vision,
  or other classes, run additionally:
    ```shell
    conda -y install pip scipy pandas jupyter \
                     scikit-learn scikit-image
    ```

[^IDE]: Integrated Development Environment


# The last slide

![You're a turtle! (xkcd.com/889)](https://imgs.xkcd.com/comics/turtles.png)
