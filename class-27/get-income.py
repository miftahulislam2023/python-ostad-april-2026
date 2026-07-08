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
def get_income_by_id():
    id = int(input("Enter the income ID to show: "))
    for income in incomes:
        if income["income_id"] == id:
            print(income)
            break
    else:
        print("Income not found")

get_income_by_id()