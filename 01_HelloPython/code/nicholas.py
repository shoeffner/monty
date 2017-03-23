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
