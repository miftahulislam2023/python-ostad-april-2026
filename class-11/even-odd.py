# Even or Odd

number = int(input("Enter a number: "))
isEven = True #Flag

if number % 2 != 0:
    isEven = False

if isEven:
    print("Even")
else:
    print("Odd")