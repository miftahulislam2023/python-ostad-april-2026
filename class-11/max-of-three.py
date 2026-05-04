# a, b, c

a = float(input())
b = float(input())
c = float(input())

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)
    