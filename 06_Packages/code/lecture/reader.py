def read_data(filename):
    """Reads a comma separated file into a list of lists.
    Each sublist contains floats.

    Args:
        filename: the file to read.

    Returns:
        A list of lists containing floats, e.g.:
        [[1., 2., 1.4],
         [2., 1.4, 3.]]
    """
    with open(filename, 'r') as in_file:
        data = in_file.read().splitlines()
    for i, row in enumerate(data):
        data[i] = [float(x) for x in row.split(',')]
    return data
