# Pattern Printing 4
"""
*****
*   *
*   *
*   *
*   *
*   *
*****
"""
r = int(input("Row:"))
c = int(input("Column:"))

for i in range(r):
    if i == 0 or i == r - 1:
        for j in range(c):
            print("*", end=" ")
    else:
        for j in range(c):
            if j == 0 or j == (c-1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()