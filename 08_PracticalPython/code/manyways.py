import string
import itertools


def loops():
    list1 = []
    for i in string.ascii_lowercase:
        list1.append(ord(i))

    list2 = []
    for i in range(1, 100):
        if i % 3 and i % 5:
            list2.append(i)

    list3 = []
    for i in range(1, 4):
        for j in range(1, 4):
            list3.append((i, j))

    list4 = []
    for i in range(1, 4):
        for j in range(1, 4):
            list4.append(i + j)

    return list1, list2, list3, list4


def lambdas():
    list1 = list(map(ord, string.ascii_lowercase))

    list2 = list(filter(lambda x: x % 3 and x % 5, range(1, 100)))

    list3 = list(itertools.product(range(1, 4), range(1, 4)))

    list4 = list(map(sum, itertools.product(range(1, 4), range(1, 4))))

    return list1, list2, list3, list4


def list_comprehensions():
    list1 = [ord(s) for s in string.ascii_lowercase]

    list2 = [x for x in range(1, 100) if x % 3 and x % 5]

    list3 = [(x, y) for x in range(1, 4) for y in range(1, 4)]

    list4 = [x + y for x in range(1, 4) for y in range(1, 4)]

    return list1, list2, list3, list4


def main():
    print('Loops:')
    print(*loops(), sep='\n')
    print('Lambdas:')
    print(*lambdas(), sep='\n')
    print('List comprehensions:')
    print(*list_comprehensions(), sep='\n')


if __name__ == '__main__':
    main()
