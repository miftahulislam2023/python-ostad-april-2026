from datetime import datetime
incomes = [
    {
        "income_id": 1,
        "category": "Salary",
        "short_description": "Teaching",
        "description": "Teaching income from XYZ Platform",
        "amount": 10000,
        "date": "2026-07-01",
        "date_created": "2026-07-01",
        "date_updated": "2026-07-01"
    },
    {
        "income_id": 2,
        "category": "Freelancing",
        "short_description": "Freelancing",
        "description": "Freelancing income from ABC Platform",
        "amount": 25000,
        "date": "2026-07-02",
        "date_created": "2026-07-02",
        "date_updated": "2026-07-02"
    }
]

def add_income():
    income_id = len(incomes) + 1 
    date_created = datetime.now().strftime("%Y-%m-%d")
    date_updated = datetime.now().strftime("%Y-%m-%d")

    category = input("Category: ")
    short_description = input("Short Description: ")
    description = input("Description: ")
    amount = input("Amount: ")
    date = input("Date: ")

    incomes.append({
        "income_id": income_id,
        "category": category,
        "short_description": short_description,
        "description": description,
        "amount": amount,
        "date": date,
        "date_created": date_created,
        "date_updated": date_updated
    })
    print("Income added successfully")

add_income()

"""
   - ID (auto-generated, unique)
   - DateCreated (auto-generated, default - current date)
   - DateUpdated (auto-generated, default - current date)
   - Category (optional, default - uncategorized)
   - Short Description (required)
   - Description (optional)
   - Amount (required, must be positive)
   - Date (optional, default - current date)
"""