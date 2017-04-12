import math


def add(x, y):
    result = []
    for i, x_i in enumerate(x):
        result.append(x_i + y[i])
    return result


def sub(x, y):
    result = []
    for i, x_i in enumerate(x):
        result.append(x_i - y[i])
    return result


def dot(x, y):
    result = 0
    for i, x_i in enumerate(x):
        result = result + x_i * y[i]
    return result


def angle(x, y):
    origin = [0 for i in range(len(x))]
    return math.acos(dot(x, y) / (pdist(x, origin) * pdist(y, origin)))


def pdist(x, y, p=2):
    result = 0
    for i, x_i in enumerate(x):
        result = result + (x_i - y[i]) ** p
    return result ** (1 / p)


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [0, 1, 0, 0, 1]
    d = [1.5, 2.5, 3.5, 4.5, 5.5]

    print("1. Expected: [5, 7, 9]\nActual: {}\n".format(add(a, b)))
    print("2. Expected: [5, 7, 9]\nActual: {}\n".format(add(b, a)))
    print("3. Expected: [-3, -3, -3]\nActual: {}\n".format(sub(a, b)))
    print("4. Expected: 8.0\nActual: {}\n".format(dot(c, d)))
    print("5. Expected: ~5.2\nActual: {}\n".format(pdist(a, b)))
    print("6. Expected: ~5.6\nActual: {}\n".format(pdist(c, d, 4)))
    print("7. Expected: ~0.23\nActual: {}\n".format(angle(a, b)))
