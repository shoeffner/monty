import time
import turtle

LENGTH = 5
ANGLE = 40


def draw_tree(h):
    if h == 0:
        return
    turtle.forward(LENGTH * h)
    turtle.left(ANGLE)
    draw_tree(h - 1)
    turtle.right(2 * ANGLE)
    draw_tree(h - 1)
    turtle.left(ANGLE)
    turtle.backward(LENGTH * h)


def draw_house():
    height = 5
    width = 7
    roofside = (width ** 2 / 2) ** (1 / 2)
    turtle.forward(LENGTH * height)  # left wall
    turtle.right(45)  # roof
    turtle.forward(LENGTH * roofside)
    turtle.right(90)
    turtle.forward(LENGTH * roofside)
    turtle.right(45)
    turtle.forward(LENGTH * height)  # right wall
    turtle.right(90)
    turtle.forward(LENGTH * width)  # bottom line
    turtle.right(90)


def init():
    turtle.reset()
    turtle.shape('turtle')
    turtle.speed('fastest')


def draw_example():
    init()
    turtle.left(90)
    turtle.up()
    turtle.goto(-100, 0)
    turtle.down()

    draw_house()

    turtle.up()
    turtle.goto(100, 0)
    turtle.down()

    draw_tree(5)


def draw_flat_world():
    init()
    turtle.up()
    turtle.goto(-400, 0)

    for i in range(8):
        turtle.down()
        turtle.left(90)
        draw_house()
        turtle.right(90)
        turtle.up()
        turtle.forward(LENGTH * 11)
        for j in range(3):
            turtle.down()
            turtle.left(90)
            if j % 2 == 0:
                draw_tree(3)
            else:
                draw_tree(5)
            turtle.right(90)
            turtle.up()
            turtle.forward(LENGTH * 3)
        turtle.forward(LENGTH)


def draw_round_world():
    init()
    turtle.ht()
    turtle.up()
    turtle.goto(0, 300)

    for i in range(18):
        turtle.down()
        turtle.left(90)
        draw_house()
        turtle.right(95)
        turtle.up()
        turtle.forward(LENGTH * 11)
        for j in range(3):
            turtle.down()
            turtle.left(90)
            if j % 2 == 0:
                draw_tree(3)
            else:
                draw_tree(5)
            turtle.right(95)
            turtle.up()
            turtle.forward(LENGTH * 3)


draw_example()
time.sleep(10)
draw_flat_world()
# time.sleep(10)
# draw_round_world()

turtle.done()
