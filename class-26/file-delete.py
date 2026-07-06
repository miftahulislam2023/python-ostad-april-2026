import os
# os.remove("habijabi.py")
# os.remove("print_numbers.py")
# os.remove("class-26/ha.txtx")
input = input("Do you really want to delete the file ha.txt? (y/n): ")
if input.lower() == "y":
    os.remove("/Users/miftahulislam/Programming/python/python-ostad-april-2026/class-26/ha.txt")
    print("File deleted successfully")
else:
    print("File not deleted")