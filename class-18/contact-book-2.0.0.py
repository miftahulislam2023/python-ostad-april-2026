# initialize an empty list of contacts
contacts = []

# input the number of contacts to be taken
n = int(input("How many contacts do you want to input? "))

for i in range(n):
    # print the current contact number to be taken
    if i == 0:
        ordinal_number = f"{i + 1}st"
    elif i == 1:
        ordinal_number = f"{i + 1}nd"
    elif i == 2:
        ordinal_number = f"{i + 1}rd"
    else:
        ordinal_number = f"{i + 1}th"

    print(f"Enter {ordinal_number} contact info: ")

    # take input from user
    name = input("Name: ")
    phone = input("Phone number: ")

    # define a temporary contact for appending
    temporary_contact = {
        "name": name,
        "phone": phone
    }

    # append to the contacts list
    contacts.append(temporary_contact)

# print contacts
for i in range(len(contacts)):
    print(f"{i + 1}. {contacts[i]["name"]}: {contacts[i]["phone"]}")