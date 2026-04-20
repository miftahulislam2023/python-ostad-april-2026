# Leap Year
"""
IF (year % 400 == 0) THEN "Leap Year"
ELSE IF (year % 100 == 0) THEN "Not Leap Year"
ELSE IF (year % 4 == 0) THEN "Leap Year"
ELSE "Not Leap Year"
"""

year = int(input("Enter a year: "))
if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not leap year")
elif year % 4 == 0: #modulus operator
    print("Leap year")
else:
    print("Not leap year")