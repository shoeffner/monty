upright = (-1, 1)
down = (1, 0)


def init(order):
    square = [[0] * order for i in range(order)]
    square[0][order // 2] = 1
    return square, (0, order // 2)


def solved(square):
    for row in square:
        if not all(row):
            return False
    return True


def magic(square, position, number=1):
    if solved(square):
        return True
    for yoff, xoff in [upright, down]:
        y = (position[0] + yoff) % len(square)
        x = (position[1] + xoff) % len(square[0])
        if square[y][x] == 0:
            square[y][x] = number + 1
            if magic(square, (y, x), number + 1):
                return True
            else:
                square[y][x] = 0
    return False


square, position = init(3)
magic(square, position)
print('\n'.join(str(row) for row in square))
