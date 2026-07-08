# Class 27

## Today's Topic
- Mini Project – Expense Tracker or File Note App

## Expense Tracker Program
### Requirements
#### Sections
1. Expense
   - ID (auto-generated, unique)
   - Category (optional, default - uncategorized)
   - Short Description (required)
   - Description (optional)
   - Amount (required, must be positive)
   - Date (optional, default - current date)
   - DateCreated (auto-generated, default - current date)
   - DateUpdated (auto-generated, default - current date)
2. Income
   - ID (auto-generated, unique)
   - Category (optional, default - uncategorized)
   - Short Description (required)
   - Description (optional)
   - Amount (required, must be positive)
   - Date (optional, default - current date)
   - DateCreated (auto-generated, default - current date)
   - DateUpdated (auto-generated, default - current date)
3. Category
   - ID (auto-generated, unique)
   - Title (required, unique per type)
   - Description (optional)
   - Type (EXPENSE | INCOME)
   - DateCreated (auto-generated, default - current date)
   - DateUpdated (auto-generated, default - current date)
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

## Homework
1.  TODO List (title, description, id)
   - Item Add
   - Item Update
   - Item Delete
   - Item Search
   - Item Filter
   - Item Pagination
   - Item Get by ID