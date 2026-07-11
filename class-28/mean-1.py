# Average of some numbers
numbers = (input("Enter some numbers: ")).split()
# print(numbers)
# print(type(numbers))

sum = 0
for i in numbers:
    sum += int(i)

print(sum)
print(sum / len(numbers))