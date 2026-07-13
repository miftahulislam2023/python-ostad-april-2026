numbers = [12, 10, 9, 1, 2, 4, 5, 30, 23, -5, 6]
ascending = [-5, 1, 2, 4, 5, 6, 9, 10, 12, 23, 30] # ascending -> ছোট থেকে বড়
descending = [30, 23, 12, 10, 9, 6, 5, 4, 2, 1, -5] # descending -> বড় থেকে ছোট

# Warning! আপনি আজকে বুঝবেন না।

n = len(numbers)
i = 1
# outer loop -> either largest item কে শুরুতে নেওয়া or শেষে নেওয়া
while i < n:
    j = 0

    # inner loop -> exchange করা
    while j < n - i:
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        
        j += 1
    
    i += 1

print(numbers)

"""
[23, 12], 45, 1, 5, 2
12, [23, 45], 1, 5, 2
12, 23, [45, 1], 5, 2
12, 23, 1, [45, 5], 2
12, 23, 1, 5, [45, 2]

12, 23, 1, 5, 2, 45

2nd cycle:
[12, 23], 1, 5, 2
12, [23, 1], 5, 2
12, 1, [23, 5], 2
12, 1, 5, [23, 2]

12, 1, 5, 2, 23

3rd cycle:
[12, 1], 5, 2
1, [12, 5], 2
1, 5, [12, 2]

1, 5, 2, 12

4th cycle:
[1, 5], 2
1, [5, 2]

1, 2, 5


5th cycle:
[1, 2]

1, 2
"""