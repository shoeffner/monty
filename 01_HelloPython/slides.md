% Basic Programming in Python: Hello Python!
% Aline Vilks, Sebastian Höffner


# Hello Python!

```python
print('Hello Python!')
```


# Programming is easy

But it takes a lot of time to become good at it.

It's like sports: It's easy to run, but it takes a lot of practice to run a marathon.

You need ten thousands of hours to master a skill -- we can only present you with your first 50 or so.


# Why programming?

## Programming in academia

* Course work focuses more on contents, less on tools
* Data analysis becomes more fluent
* Theses and papers become easier
* You learn to automate things to be more productive

## Programming outside of academia

* Understanding the principles helps with every day tasks:
    - using office programs
    - filing your tax returns
    - understanding insurance policies
    - ...
* Understanding technology makes things easier and less magic
* Basically every single job for academic people involves code


# Questionnaire results

[Responses](https://docs.google.com/forms/d/17k-BJSgCRWh1cFf86YJNKBTFgrlwza-4l34wv0EBG-8/edit#responses)


# Lecture

- Time:
- Room:

(Complete list in Stud.IP)


# Homeworks

- One sheet per week
- Deadline is before Monday morning, 08:00
- In groups of N students
- Sign up on Stud.IP


# Feedback sessions

- Once per week
- Homeworks will be checked and commented on
- Not a bad thing, but an opportunity!


# Grading

- Only Fail/Pass
- To Pass: TODO


# Let's learn together

## Ask questions
- Ask questions in class
- Ask questions in the [forum](TODO)
- Ask questions per mail

## Share your knowledge
- Collect your error messages and the code which produces them here: TODO
- Try to solve them
- We will have a session soon where we discuss different errors


# Let's program!

We will very often see Pseudocode, algorithms written down in a concise way but
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

[^print]: printing means to output something, usually on the terminal. Don't
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

`Hello World!` programs give us an idea of how a language looks like.
There are other demo programs but we will take a look into some later.

Keep in mind: the concepts are always very very similar!


# Your first homework

Setup your laptop to run python (we will discuss this in a minute).
Write your own `Hello World!` program.


# Installation of Python (Windows)

* Download Python 3.6 from [https://www.python.org/](https://www.python.org/) (Careful with 32 and 64 bit versions!)
* Install it and make sure that "Add Python 3.6 to PATH" is selected during the installation.
* Download spyder from [http://www.lfd.uci.edu/~gohlke/pythonlibs/#spyder](http://www.lfd.uci.edu/~gohlke/pythonlibs/#spyder), use `spyder-3.1.3-py3-none-any.whl`.
* Open your Command Prompt and install it
    ```shell
    pip install [...]
    ```
    Replace `[...]` with the path to the downloaded file, e.g.
    ```shell
    pip install C:\Users\Basti\Downloads\spyder-3.1.3-py3-none-any.whl
    ```


# Installation of Python (Mac OS)

* Follow the "Install Homwbrew" instructions (copy the line into the Terminal and excute it).
* Install Python 3.6 with:
    ```shell
    brew install python3
    ```
* Install spyder with
    ```shell
    pip3 install spyder
    ```


# Installation of Python (Ubuntu)

* On Ubuntu versions less than 16.10 run
    ```shell
    sudo add-apt-repository ppa:jonathonf/python-3.6
    ```
* Then, on all Ubuntu versions, install Python 3.6 with:
    ```shell
    sudo apt-get update
    sudo apt-get install -y built-essentials python3.6
    ```
* Install spyder with `pip3 install spyder`

