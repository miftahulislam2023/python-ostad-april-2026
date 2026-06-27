def outer():
    x = 7
    y = 3

    print(x + y)
    def inner(x, y):
        print(x + y)
    inner(23, 45)

outer()