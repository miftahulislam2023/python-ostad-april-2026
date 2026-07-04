"""
1. Addition
2. Subtraction
3. Mulplication
4. Division
"""
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    if y != 0:
        return x / y
    else:
        print("Division by zero is not allowed")

print("1. Addition")
print("2. Subtraction")
print("3. Mulplication")
print("4. Division")

choice = int(input("Enter your choice: "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
    print("Result: ", add(num1, num2))
elif choice == 2:
    print("Result: ", sub(num1, num2))
elif choice == 3:
    print("Result: ", mul(num1, num2))
elif choice == 4:
    print("Result: ", div(num1, num2))
else:
    print("Invalid choice")

print(div(12, 45))