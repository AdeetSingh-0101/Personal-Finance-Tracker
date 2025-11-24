Project Requirements: Personal Finance Tracker (Python CLI):-
***********************************************************

This document outlines the functional and non-functional requirements for the Personal Finance Tracker, a command-line interface (CLI) application designed to help users manage and summarize their daily financial transactions.

1. Functional Requirements (FR):-
   *****************************
 FR 1.0 - Core Transaction Management (CRUD)
                         -------------
 FR 1.1 - Add Transaction
  Status: Complete
  Description: The user must be able to input the type (Income/Expense), amount, category, and a description for a new transaction. The date should be automatically recorded as the current date.
                         -------------
 FR 1.2 - View All Transactions
  Status: Complete
  Description: The user must be able to display a formatted list of all recorded transactions, including Date, Type, Amount, Category, and Description.
                         -------------
 FR 1.3 - Clear All Transactions
  Status: Complete
  Description: The user must be able to reset the data file, removing all recorded transactions after a confirmation prompt.
                         -------------
 FR 1.4 - Delete Individual Transaction
  Status: Pending
  Description: The user must be able to view transactions with an index and select one index to permanently delete a single record from the data file.
                         -------------
 FR 1.5 - Edit Transaction
  Status: Pending
  Description: The user must be able to select a transaction by index and modify any of its fields (Date, Type, Amount, Category, Description).
____________________________________________________________________________________________

FR 2.0 - Data Validation and Integrity:-
****************************************
 FR 2.1 - Amount Validation
  Status: Complete
  Description: The system must only accept positive numeric values for the transaction amount.
                         -------------
 FR 2.2 - Type Validation
  Status: Complete
  Description: The system must only accept 'I' (Income) or 'E' (Expense) for the transaction type.
                         -------------
 FR 2.3 - Category Mapping
  Status: Complete
  Description: The system must dynamically display and validate category choices based on the transaction type ('I' or 'E').
                         -------------
 FR 2.4 - Data Persistence
  Status: Complete
  Description: All transaction data must be persistently stored in a local CSV file (transactions.csv).
_____________________________________________________________________________________________
FR 3.0 - Reporting and Analysis:-
********************************
  
 FR 3.1 - Generate Summary
  Status: Complete
  Description: The system must calculate and display the total income, total expense, and the net balance (Income - Expense).
                         -------------
 FR 3.2 - Categorical Breakdown Report
  Status: Pending
  Description: The system must generate a detailed report showing the total amount spent for each expense category and the total amount received for each income category.
                         -------------
 FR 3.3 - Filtering by Date
  Status: Pending
  Description: The system must allow users to filter transactions and the summary report based on a user-defined date range (e.g., month or year).
_____________________________________________________________________________________________
FR 4.0 - User Interface (CLI Menu):-
**********************************

 FR 4.1 - Main Menu Display
  Status: Complete
  Description: The user must be presented with a numbered menu of available options (Add, View, Summary, Clear, Exit).
                         -------------
 FR 4.2 - Exit Functionality
  Status: Complete
  Description: The system must allow the user to gracefully exit the application.
____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
2. Non-Functional Requirements (NFR):-
**************************************
**************************************


NFR 1.0 - Usability and Maintainability:-
***************************************
 NFR 1.1 - User-Friendly Input
  Description: All user prompts must be clear, guiding the user on the required input format and valid choices.
                         -------------
 NFR 1.2 - Code Maintainability
  Description: The code must be modular (using functions), well-commented, and follow Python style conventions (PEP 8).
                         -------------
 NFR 1.3 - Cross-Platform
  Description: The CLI application must run successfully on standard Windows, macOS, and Linux Python environments.
_____________________________________________________________________________________________
NFR 2.0 - Reliability and Performance:-
**************************************

 NFR 2.1 - Graceful Error Handling
  Description: The system must include try...except blocks to handle non-critical file read/write errors and invalid user input without crashing.
                         -------------
 NFR 2.2 - Data Initialization
  Description: The system must automatically create the necessary data file with correct headers if it does not exist.
                         -------------
 NFR 2.3 - Performance (Data Size)
  Description: The application must maintain sub-second response times for all functions for transaction files up to 10,000 records.
____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

3. Technology Stack:-
*******************
Component: Programming Language
Technology: Python 3
Rationale: Core language for development.

Component: Data Storage
Technology: CSV (Comma Separated Values)
Rationale: Simple, persistent local storage format for basic data management.

Component: Standard Libraries
Technology: csv, datetime, os
Rationale: Used for file operations, time-stamping, and standard data handling.



???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????