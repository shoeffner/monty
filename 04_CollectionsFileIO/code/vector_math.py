import math


def add(x, y):
    """Adds two vectors x and y.

    Args:
        x: The first summand.
        y: The right summand.

    Returns:
        The result is the vector z for which z_i = x_i + y_i holds.
    """
    result = []
    for i, x_i in enumerate(x):
        result.append(x_i + y[i])
    return result


def sub(x, y):
    """Subtracts two vectors x and y.

    Args:
        x: The minuend.
        y: The subtrahend.

    Returns:
        The result is the vector z for which z_i = x_i - y_i holds.
    """
    result = []
    for i, x_i in enumerate(x):
        result.append(x_i - y[i])
    return result


def dot(x, y):
    """Calculates the scalar product between two vectors x and y.

    The scalar product is the sum of the products of each individual elements.

    Args:
        x: The left multiplicand.
        y: The right multiplicand.

    Returns:
        The sum of all z_i for which z_i = x_i * y_i holds.
    """
    result = 0
    for i, x_i in enumerate(x):
        result = result + x_i * y[i]
    return result


def angle(x, y):
    """Calculates the angle between two vectors x and y.

    Uses the definition of the scalar product <x, y>:

        <x, y> = |x| |y| cos(alpha)

    where |x| is the norm of x.

    The function uses the distance between the two points and the origin
    respectively to calculate the respective norms.

    Args:
        x: The first vector.
        y: The second vector.

    Returns:
        The angle between the two vectors.
    """
    return math.acos(dot(x, y) / math.sqrt(dot(x, x) * dot(y, y)))


def pdist(x, y, p=2):
    """Calculates the p-distance between x and y.

    The p-distance between two points is the p-th root of the sum over all
    (x_i - y_i) ^ p.

    By default, the p=2 distance is returned, which is also known as the
    euclidean distance.

    Args:
        x: One point.
        y: Another point.

    Returns:
        The p-distance between x and y.
    """
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
