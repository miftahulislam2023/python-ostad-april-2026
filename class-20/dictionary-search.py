contacts = [
    {
        "name": "Miftahul Islam",
        "phone": "01742855755"
    },
    {
        "name": "Abdur Rahman",
        "phone": "01812345678"
    },
    {
        "name": "Fatema Khatun",
        "phone": "01923456789"
    },
    {
        "name": "Hasan Mahmud",
        "phone": "01612345678"
    },
    {
        "name": "Sadia Islam",
        "phone": "01552345678"
    },
    {
        "name": "Kamrul Islam",
        "phone": "01798765432"
    },
    {
        "name": "Nusrat Jahan",
        "phone": "01876543210"
    },
    {
        "name": "Rakib Ahmed",
        "phone": "01987654321"
    },
    {
        "name": "Tania Akter",
        "phone": "01676543210"
    },
    {
        "name": "Mahbub Alam",
        "phone": "01511223344"
    },
    {
        "name": "Shuvo Das",
        "phone": "01712398765"
    },
    {
        "name": "Jannatul Ferdous",
        "phone": "01823498765"
    },
    {
        "name": "Arif Hossain",
        "phone": "01934598765"
    }
]

search_term = ""

while search_term != ':q':
    search_term = input("Enter name or phone number to search: ")
    if search_term == ":q":
        print("Exiting...")
        break
    found_contact = False
    for contact in contacts:
        if (contact["name"] == search_term) or (contact["phone"] == search_term):
            print(f"Contact found: {contact["name"]} - {contact["phone"]}")
            found_contact = True
    if not found_contact:
        print("Contact not found")

