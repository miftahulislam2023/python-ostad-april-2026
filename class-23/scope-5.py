def outer():
    x = 7
    y = 3

    print(x + y)
    def inner():
        print(x + y)
    inner()

outer()