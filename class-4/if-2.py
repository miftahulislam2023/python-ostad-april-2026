# Adult or Not
age = int(input('Enter your age: '))
if age >= 16:
    print("Adult")
elif age >= 0 and age < 16:
    print("Not adult")
else:
    print("Invalid age")