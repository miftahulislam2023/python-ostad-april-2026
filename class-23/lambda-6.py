def add(x, y):
    x = x ** 2
    y = y - 10
    print(x + y)

add_lambda = lambda x, y: print(x + y)

add(12, 65)
add_lambda(12, 65)