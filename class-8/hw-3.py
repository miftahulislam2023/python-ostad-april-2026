# Print all even numbers between two integers
start = int(input("Start:"))
end = int(input("End:"))

if start % 2 == 0:
    # start = 4
    while start <= end:
        print(start)
        start += 2
else:
    start += 1 # start = 3
    while start <= end:
        print(start)
        start += 2