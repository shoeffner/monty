import requests


def maybe_float(v):
    """Casts a value to float if possible.

    Args:
        v: The value to cast.

    Returns:
        A float, or the original value if a cast was not possible.
    """
    try:
        return float(v)
    except ValueError:
        return v


def iris_data():
    """Attempts to read the iris.data file.

    If the iris.data is not found, it will be downloaded from the UCI ML
    repository.

    Returns:
        A list of data rows from the iris data file and the labels:

        [[1.2, 4.3, 1.4, 3.2, 'Iris-setosa'], [...]], ['Sepal length', ...]
    """
    try:
        with open('iris.data', 'r') as iris_file:
            data = iris_file.read()
    except FileNotFoundError:
        url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
        data = requests.get(url).text
        with open('iris.data', 'w') as iris_file:
            iris_file.write(data)

    return ([list(map(maybe_float, l.split(',')))
             for l in data.splitlines() if l],
            ['Sepal length', 'Sepal Width', 'Petal Length', 'Petal Width',
             'Class'])
