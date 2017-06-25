import requests


def maybe_float(v):
    try:
        return float(v)
    except ValueError:
        return v


def iris_data():
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
