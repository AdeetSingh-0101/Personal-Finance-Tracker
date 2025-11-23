# Personal-Finance-Tracker
The Personal Finance Tracker is a foundational Computer Science project developed in Python, designed to demonstrate core programming principles, file handling, and data reporting. This application operates via a Command Line Interface (CLI), making it lightweight and focusing entirely on backend logic.
...................................................................................

Personal Finance Tracker (Fresher)
******** ******* ******* *********

A simple, command-line interface (CLI) application built in Python for tracking personal income and expenses. All transaction data is securely stored locally in a CSV file (transactions.csv).
.....................................................................................

✨ Features:-
*************
    This application provides the following core functionalities:

    Add New Transaction: Easily record income or expense details, including the type, amount, a specific category, and a description.

    View All Transactions: Display a detailed, formatted list of every transaction ever recorded.

    Generate Summary: Calculate and display the total income, total expenses, and the resulting net balance (Surplus or Deficit).

    Clear All Transactions: A destructive function to delete the transaction file and start over, useful for testing or periodic reset.

    Data Persistence: All data is saved automatically to transactions.csv after every transaction and loaded upon startup.
...................................................................................

🚀 Getting Started:-
*********************
   Prerequisites

   You only need Python installed on your system. This application was built using standard Python libraries, so no additional dependencies (like pip install requirements) are needed.

   Python 3.x
......................................................................................

How to Run:-
***********
    Save the Python script as finance_tracker.py.

    Open your terminal or command prompt.

    Navigate to the directory where you saved the file.

    Run the application using the Python interpreter:

    python finance_tracker.py


    The application will automatically create the transactions.csv file if it doesn't already exist and present you with the main menu.
.......................................................................................


🛠️ Usage Example:-
*****************
The application guides you through the process using numbered menu options:

==================================
PERSONAL FINANCE TRACKER (FRESHER)
==================================
1. Add New Transaction
2. View All Transactions
3. Generate Summary (Income/Expense/Balance)
4. Clear All Transactions
5. Exit and Save
Enter your choice (1-5): 1

--- ADD TRANSACTION ---
Enter Type (I for Income / E for Expense): E
Enter Amount (e.g., 150.50): 45.75

Available Categories for EXPENSE:
  1. Food
  2. Transport
  3. Rent
  4. Utilities
  5. Entertainment
  6. Other
Enter Category number (1-6): 1
Enter a brief Description: Dinner at favorite restaurant
....................................................
✅ Transaction successfully recorded!

...

Enter your choice (1-5): 3

--- FINANCIAL SUMMARY ---
Total Income:     $1,500.00
Total Expense:    $345.75
------------------------------
Net Balance:      $1,154.25 (Surplus)
...........................................................................................


⚙️ Data Structure and Configuration:-
************************************
    Data File

    All data is stored in:

    transactions.csv

    The file uses the following headers: Date, Type, Amount, Category, Description.
.....................................................................................
Categories:-
***********
    The available categories are defined within the script. You can easily modify them in the CATEGORIES dictionary in the finance_tracker.py file:
.....................................................................................
 CATEGORIES = {
    'E': ['Food', 'Transport', 'Rent', 'Utilities', 'Entertainment', 'Other'],
    'I': ['Salary', 'Freelance', 'Investment', 'Gift', 'Other Income']
 }

.....................................................................................
 Date Format:-
*************
     The date is automatically recorded using the YYYY-MM-DD format.


<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>