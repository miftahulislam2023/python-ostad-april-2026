def habijabi(x, y, z):
    x = x * 10
    return x + y - z * x / y + z

habijabi_lambda = lambda x, y, z: x + 10
print(habijabi(1, 2, 3))
print(habijabi_lambda(1, 2, 3))