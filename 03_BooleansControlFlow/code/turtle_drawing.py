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


def draw_world(curvature_step=0):
    if curvature_step > 0:
        villages = 360 // 4 // curvature_step
    else:
        villages = 5

    for i in range(villages):
        prepare_drawing()
        draw_house()
        finish_drawing()

        turtle.right(curvature_step)
        turtle.forward(LENGTH * 11)

        for j in range(3):
            prepare_drawing()
            draw_tree(3 + j % 2 * 2)
            finish_drawing()

            turtle.right(curvature_step)
            turtle.forward(LENGTH * 3)

        turtle.forward(LENGTH)


def init():
    turtle.reset()
    turtle.shape('turtle')
    turtle.speed('fastest')
    turtle.up()


def prepare_drawing():
    turtle.down()
    turtle.left(90)


def finish_drawing():
    turtle.right(90)
    turtle.up()


def draw_flat_world():
    init()
    turtle.goto(-300, 0)

    draw_world()


def draw_round_world():
    init()
    turtle.goto(0, 300)
    turtle.hideturtle()

    draw_world(5)


def draw():
    draw_flat_world()
    time.sleep(5)
    draw_round_world()
    turtle.done()


draw()
