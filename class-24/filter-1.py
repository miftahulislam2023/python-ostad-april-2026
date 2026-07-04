"""
filter বোঝা কেন কঠিন? 
১। এটি একটি হায়ার অর্ডার ফাংশন
২। এটি ফিল্টার করে যে ফাংশন পাস করা হয় সেই শর্তানুসারে
৩। ল্যম্বডা ফাংশন ব্যবহার করলে আর কঠিন হয়ে যায় অনেকের জন্য

filter(function, iterable)

function: একটি শর্তযুক্ত ফাংশন যা True অথবা False রিটার্ন করে।
iterable: আপনার মূল ডাটা।
"""
numbers = [
    {
        "phone":"01783940182",
        "total_otp": 12
    },
    {
        "phone": "01349201847",
        "total_otp": 8
    },
    {
        "phone": "01823948102",
        "total_otp": 15
    },
    {
        "phone": "01674920183",
        "total_otp": 3
    },
    {
        "phone": "01938401928",
        "total_otp": 6
    },
    {
        "phone": "01482910384",
        "total_otp": 14
    },
    {
        "phone": "01558291038",
        "total_otp": 7
    },
    {
        "phone": "01711039482",
        "total_otp": 11
    },
    {
        "phone": "01847291038",
        "total_otp": 4
    },
    {
        "phone": "01623948105",
        "total_otp": 19
    },
    {
        "phone": "01911029384",
        "total_otp": 2
    },
    {
        "phone": "01712345678",
        "total_otp": 5
    },
    {
        "phone": "01512345678",
        "total_otp": 10
    },
    {
        "phone": "01612345678",
        "total_otp": 1
    },
    {
        "phone": "01812345678",
        "total_otp": 18
    },
    {
        "phone": "01912345678",
        "total_otp": 13
    },
    {
        "phone": "01312345678",
        "total_otp": 9
    },
    {
        "phone": "01412345678",
        "total_otp": 16
    },
    {
        "phone": "01787654321",
        "total_otp": 20
    },
    {
        "phone": "01587654321",
        "total_otp": 0
    },
    {
        "phone": "01687654321",
        "total_otp": 17
    },
    {
        "phone": "01887654321",
        "total_otp": 5
    },
    {
        "phone": "01987654321",
        "total_otp": 12
    },
    {
        "phone": "01387654321",
        "total_otp": 7
    },
    {
        "phone": "01487654321",
        "total_otp": 11
    },
    {
        "phone": "01755555555",
        "total_otp": 8
    },
    {
        "phone": "01555555555",
        "total_otp": 3
    },
    {
        "phone": "01655555555",
        "total_otp": 14
    },
    {
        "phone": "01855555555",
        "total_otp": 6
    },
    {
        "phone": "01955555555",
        "total_otp": 10
    },
    {
        "phone": "01355555555",
        "total_otp": 15
    },
    {
        "phone": "01455555555",
        "total_otp": 2
    },
    {
        "phone": "01799999999",
        "total_otp": 9
    },
    {
        "phone": "01599999999",
        "total_otp": 13
    },
    {
        "phone": "01699999999",
        "total_otp": 4
    },
    {
        "phone": "01899999999",
        "total_otp": 18
    },
    {
        "phone": "01999999999",
        "total_otp": 1
    },
    {
        "phone": "01399999999",
        "total_otp": 11
    },
    {
        "phone": "01499999999",
        "total_otp": 5
    },
    {
        "phone": "01711111111",
        "total_otp": 12
    },
    {
        "phone": "01511111111",
        "total_otp": 7
    },
    {
        "phone": "01611111111",
        "total_otp": 16
    },
    {
        "phone": "01811111111",
        "total_otp": 8
    },
    {
        "phone": "01911111111",
        "total_otp": 3
    },
    {
        "phone": "01311111111",
        "total_otp": 14
    },
    {
        "phone": "01411111111",
        "total_otp": 6
    },
    {
        "phone": "01722222222",
        "total_otp": 10
    },
    {
        "phone": "01522222222",
        "total_otp": 15
    },
    {
        "phone": "01622222222",
        "total_otp": 2
    },
    {
        "phone": "01822222222",
        "total_otp": 9
    },
    {
        "phone": "01922222222",
        "total_otp": 13
    }
]

def filter_banglalink(number):
    return number["phone"].startswith("019")

bl_numbers = list(filter(filter_banglalink, numbers))

lambda_bl_numbers = list(filter(lambda number: number["phone"].startswith("019"), numbers))

for number in bl_numbers:
    print(f"{number["phone"]} - {number["total_otp"]}")

for number in lambda_bl_numbers:
    print(f"{number["phone"]} - {number["total_otp"]}")