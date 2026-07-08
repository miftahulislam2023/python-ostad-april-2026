"""
### Requirements
#### Sections
1. Expense
   - ID (auto-generated, unique)
   - DateCreated (auto-generated, default - current date)
   - DateUpdated (auto-generated, default - current date)
   - Category (optional, default - uncategorized)
   - Short Description (required)
   - Description (optional)
   - Amount (required, must be positive)
   - Date (optional, default - current date)
2. Income
   - ID (auto-generated, unique)
   - DateCreated (auto-generated, default - current date)
   - DateUpdated (auto-generated, default - current date)
   - Category (optional, default - uncategorized)
   - Short Description (required)
   - Description (optional)
   - Amount (required, must be positive)
   - Date (optional, default - current date)
3. Category
   - ID (auto-generated, unique)
   - DateCreated (auto-generated, default - current date)
   - DateUpdated (auto-generated, default - current date)
   - Title (required, unique per type)
   - Description (optional)
   - Type (EXPENSE | INCOME)
#### Operations
1. Income
   - Add Income
   - List Income
   - Update Income
   - Delete Income
   - Search Income (by short description, by description)
   - Filter Income (by date, by category, by amount, by month)
   - Pagination
   - Get Income by ID
2. Expense
   - Add Expense
   - List Expense
   - Update Expense
   - Delete Expense
   - Search Expense (by short description, by description)
   - Filter Expense (by date, by category, by amount, by month)
   - Pagination
   - Get Expense by ID
3. Category
   - Add Category
   - List Category
   - Update Category
   - Delete Category
   - Search Category (by title)
   - Pagination
   - Get Category by ID
"""

from datetime import datetime

incomes = []
expenses = []
categories = []

## Functions
## File Related Functions
def load_data():
    pass
def save_data():
    pass

## Income Related Functions
def add_income():
    # Auto-generated attributes
    income_id = len(incomes) + 1 
    date_created = datetime.now().strftime("%Y-%m-%d")
    date_updated = datetime.now().strftime("%Y-%m-%d")
    # User inputs
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

def list_income():
    no_of_items_to_show = int(input("How many items do you want to see? (0 for all)"))
    if no_of_items_to_show == 0:
        for income in incomes:
            print(income)
    else:
        i = len(incomes) - 1
        count = 0
        while count < no_of_items_to_show and i >= 0:
            print(incomes[i])
            i -= 1
            count += 1

def update_income():
    income_id = int(input("Enter the income ID to update: "))
    for income in incomes:
        if income["income_id"] == income_id:
            print("Press enter to keep the previous value")
            category = input(f"Category ({income['category']}): ")
            short_description = input(f"Short Description ({income['short_description']}): ")
            description = input(f"Description ({income['description']}): ")
            amount = input(f"Amount ({income['amount']}): ")
            date = input(f"Date ({income['date']}): ")
            
            income["category"] = category if category else income["category"]
            income["short_description"] = short_description if short_description else income["short_description"]
            income["description"] = description if description else income["description"]
            income["amount"] = amount if amount else income["amount"]
            income["date"] = date if date else income["date"]

            income["date_updated"] = datetime.now().strftime("%Y-%m-%d")
            print("Income updated successfully")
            break
    else:
        print("Income not found")

def delete_income():
    income_id = int(input("Enter the income ID to delete: "))
    for income in incomes:
        if income["income_id"] == income_id:
            incomes.remove(income)
            print("Income deleted successfully")
            break
    else:
        print("Income not found")

def search_income():
    search_term = input("Enter the search term: ")
    for income in incomes:
        if search_term.lower() in income["category"].lower() or search_term.lower() in income["short_description"].lower() or search_term.lower() in income["description"].lower() or search_term.lower() in income["amount"].lower() or search_term.lower() in income["date"].lower():
            print(income)
            break
    else:
        print("Income not found")

def filter_income():
    filter_by = input("Enter the field to filter by: ")
    if filter_by == "date":
        date = input("Enter the date: ")
        for income in incomes:
            if income["date"] == date:
                print(income)
    elif filter_by == "category":
        category = input("Enter the category: ")
        for income in incomes:
            if income["category"] == category:
                print(income)
    elif filter_by == "amount":
        amount = input("Enter the amount: ")
        for income in incomes:
            if income["amount"] >= amount:
                print(income)
    elif filter_by == "month":
        month = input("Enter the month: ")
        for income in incomes:
            if income["date"].split("-")[1] == month:
                print(income)
    else:
        print("Invalid filter")

def pagination_income():
    no_of_items_per_page = int(input("Enter the number of items per page: "))
    total_pages = len(incomes) // no_of_items_per_page + 1
    
    for i in range(total_pages):
        start_index = i * no_of_items_per_page
        end_index = start_index + no_of_items_per_page
        page_items = incomes[start_index:end_index]
        
        for item in page_items:
            print(item)
        
        if i < total_pages - 1:
            choice = input("Press Enter to continue to the next page, or 'q' to quit: ").lower()
            if choice == 'q':
                break

def get_income_by_id():
    id = int(input("Enter the income ID to show: "))
    for income in incomes:
        if income["income_id"] == id:
            print(income)
            break
    else:
        print("Income not found")

## Expense Related Functions
def add_expense():
    # Auto-generated attributes
    expense_id = len(expenses) + 1
    date_created = datetime.now().strftime("%Y-%m-%d")
    date_updated = datetime.now().strftime("%Y-%m-%d")
    # User inputs
    category = input("Category: ")
    short_description = input("Short Description: ")
    description = input("Description: ")
    amount = input("Amount: ")
    date = input("Date: ")

    expenses.append({
        "expense_id": expense_id,
        "category": category,
        "short_description": short_description,
        "description": description,
        "amount": amount,
        "date": date,
        "date_created": date_created,
        "date_updated": date_updated
    })
    print("Expense added successfully")

def list_expense():
    no_of_items_to_show = int(input("How many items do you want to see? (0 for all)"))
    if no_of_items_to_show == 0:
        for expense in expenses:
            print(expense)
    else:
        i = len(expenses) - 1
        count = 0
        while count < no_of_items_to_show and i >= 0:
            print(expenses[i])
            i -= 1
            count += 1

def update_expense():
    expense_id = int(input("Enter the expense ID to update: "))
    for expense in expenses:
        if expense["expense_id"] == expense_id:
            print("Press enter to keep the previous value")
            category = input(f"Category ({expense['category']}): ")
            short_description = input(f"Short Description ({expense['short_description']}): ")
            description = input(f"Description ({expense['description']}): ")
            amount = input(f"Amount ({expense['amount']}): ")
            date = input(f"Date ({expense['date']}): ")
            
            expense["category"] = category if category else expense["category"]
            expense["short_description"] = short_description if short_description else expense["short_description"]
            expense["description"] = description if description else expense["description"]
            expense["amount"] = amount if amount else expense["amount"]
            expense["date"] = date if date else expense["date"]

            expense["date_updated"] = datetime.now().strftime("%Y-%m-%d")
            print("Expense updated successfully")
            break
    else:
        print("Expense not found")

def delete_expense():
    expense_id = int(input("Enter the expense ID to delete: "))
    for expense in expenses:
        if expense["expense_id"] == expense_id:
            expenses.remove(expense)
            print("Expense deleted successfully")
            break
    else:
        print("Expense not found")

def search_expense():
    search_term = input("Enter the search term: ")
    for expense in expenses:
        if search_term.lower() in expense["category"].lower() or search_term.lower() in expense["short_description"].lower() or search_term.lower() in expense["description"].lower() or search_term.lower() in expense["amount"].lower() or search_term.lower() in expense["date"].lower():
            print(expense)
            break
    else:
        print("No expense found")

def filter_expense():
    filter_by = input("Enter the field to filter by: ")
    if filter_by == "date":
        date = input("Enter the date: ")
        for expense in expenses:
            if expense["date"] == date:
                print(expense)
    elif filter_by == "category":
        category = input("Enter the category: ")
        for expense in expenses:
            if expense["category"] == category:
                print(expense)
    elif filter_by == "amount":
        amount = input("Enter the amount: ")
        for expense in expenses:
            if expense["amount"] >= amount:
                print(expense)
    elif filter_by == "month":
        month = input("Enter the month: ")
        for expense in expenses:
            if expense["date"].split("-")[1] == month:
                print(expense)
    else:
        print("Invalid filter")

def pagination_expense():
    no_of_items_per_page = int(input("Enter the number of items per page: "))
    total_pages = len(expenses) // no_of_items_per_page + 1
    
    for i in range(total_pages):
        start_index = i * no_of_items_per_page
        end_index = start_index + no_of_items_per_page
        page_items = expenses[start_index:end_index]
        
        for item in page_items:
            print(item)
        
        if i < total_pages - 1:
            choice = input("Press Enter to continue to the next page, or 'q' to quit: ").lower()
            if choice == 'q':
                break

def get_expense_by_id():
    id = int(input("Enter the expense ID to show: "))
    for expense in expenses:
        if expense["expense_id"] == id:
            print(expense)
            break
    else:
        print("Expense not found")

## Category Related Functions
def add_category():
    # Auto-generated attributes
    category_id = len(categories) + 1
    date_created = datetime.now().strftime("%Y-%m-%d")
    date_updated = datetime.now().strftime("%Y-%m-%d")
    # User inputs
    title = input("Title: ")
    description = input("Description: ")
    type = input("Type: ")

    categories.append({
        "category_id": category_id,
        "title": title,
        "description": description,
        "type": type,
        "date_created": date_created,
        "date_updated": date_updated
    })
    print("Category added successfully")
    
def list_category():
    no_of_items_to_show = int(input("How many items do you want to see? (0 for all)"))
    if no_of_items_to_show == 0:
        for category in categories:
            print(category)
    else:
        i = len(categories) - 1
        count = 0
        while count < no_of_items_to_show and i >= 0:
            print(categories[i])
            i -= 1
            count += 1

def update_category():
    category_id = int(input("Enter the category ID to update: "))
    for category in categories:
        if category["category_id"] == category_id:
            print("Press enter to keep the previous value")
            title = input(f"Title ({category['title']}): ")
            description = input(f"Description ({category['description']}): ")
            type = input(f"Type ({category['type']}): ")
            
            category["title"] = title if title else category["title"]
            category["description"] = description if description else category["description"]
            category["type"] = type if type else category["type"]

            category["date_updated"] = datetime.now().strftime("%Y-%m-%d")
            print("Category updated successfully")
            break
    else:
        print("Category not found")

def delete_category():
    category_id = int(input("Enter the category ID to delete: "))
    for category in categories:
        if category["category_id"] == category_id:
            categories.remove(category)
            print("Category deleted successfully")
            break
    else:
        print("Category not found")

def search_category():
    search_term = input("Enter the search term: ")
    for category in categories:
        if search_term.lower() in category["title"].lower() or search_term.lower() in category["description"].lower() or search_term.lower() in category["type"].lower():
            print(category)
            break
    else:
        print("Category not found")

def pagination_category():
    no_of_items_per_page = int(input("Enter the number of items per page: "))
    total_pages = len(categories) // no_of_items_per_page + 1
    
    for i in range(total_pages):
        start_index = i * no_of_items_per_page
        end_index = start_index + no_of_items_per_page
        page_items = categories[start_index:end_index]
        
        for item in page_items:
            print(item)
        
        if i < total_pages - 1:
            choice = input("Press Enter to continue to the next page, or 'q' to quit: ").lower()
            if choice == 'q':
                break

def get_category_by_id():
    id = int(input("Enter the category ID to show: "))
    for category in categories:
        if category["category_id"] == id:
            print(category)
            break
    else:
        print("Category not found")

## Main Menu
def main_menu():
    pass