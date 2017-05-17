def read(filename):
    with open(filename, 'r') as f:
        return [{'name': name,
                 'age': int(age),
                 'height': float(height)}
                for person in f.read().splitlines()
                for name, age, height in [person.split(' ')]]


def bubblesort(bubblelist):
    bubblelist = bubblelist.copy()
    swapped = True
    while swapped:
        swapped = False
        for index in range(1, len(bubblelist[1:])):
            if bubblelist[index - 1]['height'] > bubblelist[index]['height']:
                temp = bubblelist[index]
                bubblelist[index] = bubblelist[index - 1]
                bubblelist[index - 1] = temp
                swapped = True
    return bubblelist
