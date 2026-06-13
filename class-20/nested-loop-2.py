## Pattern Printing 2
"""
*******
******
*****
****
***
"""
for i in range(5):
    for i in range(7 - i):
        print("*", end="")
    print()