import csv

with open("/Users/miftahulislam/Programming/python/python-ostad-april-2026/class-26/contact.csv", "r") as file1:
    reader = csv.reader(file1)
    # print(reader[0])
    # print(type(reader))
    i = 0
    for row in reader:
        # print(row)
        # print(type(row))
        if i != 0:
            print(f"Name: {row[0]}\tPhone: {row[1]}\tAddress: {row[2]}")
        i += 1

    