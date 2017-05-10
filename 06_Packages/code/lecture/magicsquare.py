upright = (-1, 1)
down = (1, 0)


def init(order):
    return [[0] * order for i in range(order)], (0, order // 2)


def magic(square, position, number=1):
    square[position[0]][position[1]] = number
    for yoff, xoff in [upright, down]:
        y = (position[0] + yoff) % len(square)
        x = (position[1] + xoff) % len(square[0])
        if square[y][x] == 0:
            return magic(square, (y, x), number + 1)

square, position = init(3)
magic(square, position)
print('\n'.join(str(row) for row in square))
