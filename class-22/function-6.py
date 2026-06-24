def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    # print(f"Factorial of {n} is {factorial}")
    return factorial

print(factorial(7))
print(factorial(6))
print(factorial(10))