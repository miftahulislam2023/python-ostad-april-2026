"""
Miftahul Islam - 01742855755
Abdur Rahman - 01812345678
Fatema Khatun - 01923456789
Hasan Mahmud - 01612345678
Sadia Islam - 01552345678
Kamrul Islam - 01798765432
Nusrat Jahan - 01876543210
Rakib Ahmed - 01987654321
Tania Akter - 01676543210
Mahbub Alam - 01511223344
Shuvo Das - 01712398765
Jannatul Ferdous - 01823498765
Arif Hossain - 01934598765
Lima Begum - 01645698765
Tanvir Ahmed - 01567890123
Sumaiya Parveen - 01756789012
Imran Khan - 01867890123
Rabeya Sultana - 01978901234
Farhan Ahmed - 01689012345
Mehedi Hasan - 01590123456
"""

"""
List
Tuple
Set
Dictionary
"""
# contact2 = {
# "name": "Abdur Rahman",
# "phone": "01812345678"
# }
# contact3 = {
# "name": "Fatema Khatun",
# "phone": "01923456789"
# }
# contact4 = {
# "name": "Hasan Mahmud",
# "phone": "01612345678"
# }
# contact5 = {
# "name": "Sadia Islam",
# "phone": "01552345678"
# }
# contact6 = {
# "name": "Kamrul Islam",
# "phone": "01798765432"
# }
# contact7 = {
# "name": "Nusrat Jahan",
# "phone": "01876543210"
# }
# contact8 = {
# "name": "Rakib Ahmed",
# "phone": "01987654321"
# }
# contact9 = {
# "name": "Tania Akter",
# "phone": "01676543210"
# }
# contact10 = {
# "name": "Mahbub Alam",
# "phone": "01511223344"
# }
# contact11 = {
# "name": "Shuvo Das",
# "phone": "01712398765"
# }
# contact12 = {
# "name": "Jannatul Ferdous",
# "phone": "01823498765"
# }
# contact13 = {
# "name": "Arif Hossain",
# "phone": "01934598765"
# }
# contact14 = {
# "name": "Lima Begum",
# "phone": "01645698765"
# }
# contact15 = {
# "name": "Tanvir Ahmed",
# "phone": "01567890123"
# }
# contact16 = {
# "name": "Sumaiya Parveen",
# "phone": "01756789012"
# }
# contact17 = {
# "name": "Imran Khan",
# "phone": "01867890123"
# }
# contact18 = {
# "name": "Rabeya Sultana",
# "phone": "01978901234"
# }
# contact19 = {
# "name": "Farhan Ahmed",
# "phone": "01689012345"
# }
# contact20 = {
# "name": "Mehedi Hasan",
# "phone": "01590123456"
# }

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

for i in range(len(contacts)):
    print(f"{i + 1}. {contacts[i]["name"]}: {contacts[i]["phone"]}")