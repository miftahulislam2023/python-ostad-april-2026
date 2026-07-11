is_married = input("Are you married? ")

if is_married.strip().lower() == "t" or is_married.strip().lower() == "true":
    is_married = True
elif is_married.strip().lower() == "f" or is_married.strip().lower() == "false":
    is_married = False
else:
    is_married = None

print(is_married)
print(type(is_married))