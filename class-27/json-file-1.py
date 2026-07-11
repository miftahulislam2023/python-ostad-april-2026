import json
with open("class-27/contacts.json", "r") as contact_file:
    contacts = json.load(contact_file)

print(contacts)
print(type(contacts))
print(type(contacts[0]))

for c in contacts:
    print(c["name"])