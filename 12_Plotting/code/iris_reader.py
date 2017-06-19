from csv import DictReader


def get_data():
    with open('iris.data') as iris:
        fields = ['sepal_length', 'sepal_width',
                  'petal_length', 'petal_width', 'class']
        data = list(DictReader(iris, fieldnames=fields))
        for d in data:
            for k in fields[:-1]:
                d[k] = float(d[k])
    return data

if __name__ == '__main__':
    print('\n'.join(map(str, get_data()[:3])))
