numbers = [12, 10, 9, 1, 2, 4, 5, 30, 23, -5, 6]

n = len(numbers)
i = 1
while i < n:
    j = 0
    while j < n - i:
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        j += 1
    i += 1

print(numbers)