def fizz(number):
    return number / 3 == number // 3


def buzz(number):
    return number / 5 == number // 5


def fizz_buzz(to):
    for number in range(1, to + 1):
        if buzz(number):
            if fizz(number):
                print('fizz', end='')
            print('buzz')
        elif fizz(number):
            print('fizz')
        else:
            print(number)


fizz_buzz(20)  # Play to 20
# expecting fizz: 3, 6, 9, 12, 18
# expecting buzz: 5, 10, 20
# expecting fizzbuzz: 15
