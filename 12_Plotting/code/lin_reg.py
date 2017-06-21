import statistics

def linear_regression(x, y):
    mx = statistics.mean(x)
    my = statistics.mean(y)
    b = sum((xi - mx) * (yi - my) for (xi, yi) in zip(x, y))
    b /= sum((xi - mx) ** 2 for xi in x)
    return my - b * mx, b

if __name__ == '__main__':
    from iris_reader import get_data
    data = get_data()
    x = [i['sepal_length'] for i in data if i['class'] == 'Iris-setosa']
    y = [i['sepal_width'] for i in data if i['class'] == 'Iris-setosa']
    a, b = linear_regression(x, y)
    print(a, b)
