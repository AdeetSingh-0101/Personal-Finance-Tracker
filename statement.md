Personal Finance Tracker Project Statement

This document outlines the core purpose, boundaries, target audience, and key capabilities of the Personal Finance Tracker application.
.........................................................................................

1. Problem Statement:-
********************
Many individuals struggle with maintaining clear visibility into their daily cash flow, leading to difficulties in budgeting, saving, and achieving financial goals. Existing solutions are often overly complex, require internet access, or involve subscription fees. The core problem this project addresses is the need for a simple, accessible, and free command-line tool that enables users to quickly and accurately track their income and expenses locally, facilitating better awareness and control over personal finances.
..........................................................................................

2. Scope of the Project:-
***********************
The scope of the Personal Finance Tracker is limited to the functionality available through the command-line interface and local CSV file storage.

 In Scope:
 """"""""
  Recording single-entry income and expense transactions.

  Categorizing transactions using pre-defined lists (e.g., Food, Rent, Salary).

  Generating simple aggregated summaries (Total Income, Total Expense, Net Balance).

  Data persistence via a single local file (transactions.csv).

  Out of Scope (Future Considerations):

  Graphical User Interface (GUI).

  Multi-user support or cloud synchronization.

  Advanced filtering (e.g., by date range, specific category).

  Budgeting goals, forecasting, or reporting graphs.
........................................................................................

3. Target Users:-
****************
The primary target users are individuals seeking a straightforward, non-complex solution for financial tracking.

Students/Fresh Graduates: Individuals starting their financial journey who need a simple tool to monitor spending without overwhelming features.

Minimalists: Users who prefer lightweight, terminal-based applications over heavy, resource-intensive software.

Developers/Power Users: Users comfortable with the command line who want a quick, Python-based utility for local data management.
.......................................................................................

4. High-Level Features:-
**********************
The application is built around four core functional pillars:

    Feature Area

    Description

Transaction Recording

 Allows users to input new income (I) or expense (E) records, capturing the amount, pre-defined category, and a text description.

Data Persistence

 Automatically manages a local CSV file (transactions.csv) to ensure all data is saved between sessions and is readily available.

Data Viewing

 Presents all recorded transactions in a clearly formatted list within the command-line interface.

Financial Reporting

 Calculates and displays a financial summary, including Total Income, Total Expense, and the Net Balance (indicating a Surplus or Deficit).


 <><><><><><><><<><><<><><><><><><><><><><><><><><><><><><><><><<><><><><><><><><<<<><><>><>
 <><><><><><><><<><><<><><><><><><><><><><><><><><><><><><><><><<><><><><><><><><<<<><><>><>
 <><><><><><><><<><><<><><><><><><><><><><><><><><><><><><><><><<><><><><><><><><<<<><><>><>