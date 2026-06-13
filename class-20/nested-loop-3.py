## Pattern Printing 3
"""
1
22
333
4444
55555
"""

for i in range(1, 6): # outer loop
    for j in range(i): # inner loop
        print(i, end="")
    print()
