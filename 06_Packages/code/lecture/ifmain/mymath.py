def add(a, b):
    """Adds a and b."""
    return a + b


if __name__ == '__main__':
    assert add(2, 5) == 7, '2 and 5 are not 7'
    assert add(-2, 5) == 3, '-2 and 5 are not 3'
    print('This executes only if I am main!')
