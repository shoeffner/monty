def division(x, y):
    return x / y


result = 0
for i in range(16):
    denominator = i - 10
    result += division(i, denominator)
print(result)
