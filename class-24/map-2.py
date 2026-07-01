def square(num):
    return num ** 2

numbers = [1, 2, 3, 4, 5]
result = map(square, numbers)
print(list(result))

print(list(map(lambda x: x ** 2, numbers)))