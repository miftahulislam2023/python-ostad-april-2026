"""
Print Prime Number Upto n
"""
limit = int(input("Enter a number: "))
count = 0
loop_count = 0
for x in range(2, limit):
    n = x
    isPrime = True

    for i in range(2, n):
        loop_count += 1
        if n % i == 0:
            isPrime = False
            break

    if isPrime:
        count += 1
        print(f"{count} - {x}")

print(loop_count)
# 2, 3, 5, 7
# 11, 13, 17, 19
# 23, 29
# 31, 37
# 41, 43, 47
# 53, 59
# 61, 67
# 71, 73, 79
# 83, 89
# 97

# 455,189,149