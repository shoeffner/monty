def calculator(*args, **kwargs):
    result = args[0]
    if 'operation' in kwargs.keys():
        for arg in args[1:]:
            if kwargs['operation'] == '+':
                result = result + arg
            elif kwargs['operation'] == '-':
                result = result - arg
            elif kwargs['operation'] == '*':
                result = result * arg
            elif kwargs['operation'] == '/':
                result = result / arg
    return result


print(calculator(1, 2, 3, operation='+'))
print(calculator(2, 4, 8, operation='*'))
print(calculator(3, 2, operation='-'))
print(calculator(1, 2, 3, 4, 5, 6, 7, operation='+'))
print(calculator(4, 2, 7))
print(calculator(4, 2, 7, operation='x'))
