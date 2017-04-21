def bottles(n):
    return ('1 bottle' if n == 1 else str(n) + ' bottles') + ' of beer'


def n_bottles(n):
    if not 5 <= n <= 99:
        print('I want to sing funnier songs than "' + bottles(n) + '".\n')
        return
    while n > 0:
        print(bottles(n) + ' on the wall,\n  ' + bottles(n) + '.')
        n = n - 1
        print('Take one down and pass it around,\n  ' +
              bottles(n if n > 0 else 'no more') +
              ' on the wall.\n')


n_bottles(2)
n_bottles(1013)
n_bottles(5)
