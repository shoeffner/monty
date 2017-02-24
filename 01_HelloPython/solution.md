% Exercise Sheet 01 Solutions -- Hello Python!
% Aline Vilks, Sebastian Höffner


# Exercise 1: Your development environment

For this exercise we will not include any special solutions. Instead, enjoy this little cartoon:

![How to Teach Yourself Programming](http://abstrusegoose.com/strips/ars_longa_vita_brevis.png "How to Teach Yourself Programming")


# Exercise 2: Hello you!

```python
print("Hello Aline and Basti!")

print("What's up?")

# We need escaping: \" cancels its meaning.
print("Are you \"Monty\"?")
# Alternatively you can use ':
print('Are you "Monty"?')

# But you will need escaping for the last:
print("Can't you just pretend you were \"Monty\"?")
# or
print('Can\'t you just pretend you were "Monty"?')
```

Output:

```
Hello Aline and Basti!
What's up?
Are you "Monty"?
Are you "Monty"?
Can't you just pretend you were "Monty"?
Can't you just pretend you were "Monty"?
```

# Exercise 3: Turtles all the way down

```python
import turtle


turtle.home()

# left edge
turtle.left(90)
turtle.forward(100)

# roof
turtle.right(45)
turtle.forward(70.71)
turtle.right(90)
turtle.forward(70.71)
turtle.right(135)
turtle.forward(100)

# cross and right edge
turtle.left(135)
turtle.forward(141.42)
turtle.right(45)  # !
turtle.backward(100)
turtle.right(45)
turtle.forward(141.42)

# bottom edge
turtle.left(135)
turtle.forward(100)

# keep the window open
turtle.done()
```

Result:

![St. Nicholas' house](saintnicholashouse.png "St. Nicholas' house")

