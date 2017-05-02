with open('iris.data', 'r') as iris_in, open('iris.csv', 'w') as iris_out:
    for i, line in enumerate(iris_in, 1):
        if i == 35:
            line = '4.9,3.1,1.5,0.2,Iris-setosa\n'
        if i == 38:
            line = '4.9,3.6,1.4,0.1,Iris-setosa\n'
        print(line, file=iris_out, end='')
