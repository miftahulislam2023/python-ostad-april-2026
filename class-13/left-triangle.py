"""
*
**
***
****
"""
n = int(input("Enter a number: "))
i = 1

while i <= n:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1

for i in range(n+1):
    for j in range(i):
        print("*", end="")
    print()

"""
1. pseudocode
2. dry run
3. 

"""