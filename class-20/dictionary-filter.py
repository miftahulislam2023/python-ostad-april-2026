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

filter_term = ""

while filter_term != ':q':
    # initialize
    filtered_contacts = []

    # take input from user
    filter_term = input("Enter name or phone number to filter: ")

    # exit if :q
    if filter_term == ":q":
        print("Exiting...")
        break

    # find contacts
    for contact in contacts:
        if (
            (contact["name"].lower().find(filter_term.lower()) != -1) 
        or 
            (contact["phone"].lower().find(filter_term.lower()) != -1) 
        ):
            filtered_contacts.append(contact)
    
    # print filtered contacts
    for contact in filtered_contacts:
        print(f"{contact["name"]} - {contact["phone"]}")