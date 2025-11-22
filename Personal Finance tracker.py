import csv
from datetime import datetime

# --- CONFIGURATION ---
DATA_FILE = 'transactions.csv'
CATEGORIES = {
    'E': ['Food', 'Transport', 'Rent', 'Utilities', 'Entertainment', 'Other'],
    'I': ['Salary', 'Freelance', 'Investment', 'Gift', 'Other Income']
}

def ensure_data_file():
    """Checks if the CSV data file exists and creates it with headers if it doesn't."""
    try:
        with open(DATA_FILE, 'r', newline='') as f:
            # Check if file is empty
            if f.read(1) == '':
                raise FileNotFoundError
    except FileNotFoundError:
        print(f"Creating new data file: {DATA_FILE}")
        with open(DATA_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            # Define and write the header row
            writer.writerow(['Date', 'Type', 'Amount', 'Category', 'Description'])

def add_transaction():
    """Prompts user for transaction details and adds it to the CSV file."""
    print("\n--- ADD TRANSACTION ---")

    # 1. Get Transaction Type (Income or Expense)
    while True:
        trans_type = input("Enter Type (I for Income / E for Expense): ").upper()
        if trans_type in ['I', 'E']:
            break
        print("Invalid type. Please enter 'I' or 'E'.")

    # 2. Get Amount
    while True:
        try:
            amount = float(input("Enter Amount (e.g., 150.50): "))
            if amount <= 0:
                print("Amount must be positive.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    # 3. Get Category
    print(f"\nAvailable Categories for {'INCOME' if trans_type == 'I' else 'EXPENSE'}:")
    available_cats = CATEGORIES[trans_type]
    for i, cat in enumerate(available_cats, 1):
        print(f"  {i}. {cat}")

    while True:
        try:
            cat_choice = int(input(f"Enter Category number (1-{len(available_cats)}): "))
            if 1 <= cat_choice <= len(available_cats):
                category = available_cats[cat_choice - 1]
                break
            print(f"Invalid choice. Must be between 1 and {len(available_cats)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # 4. Get Description
    description = input("Enter a brief Description: ")

    # 5. Get Date (use today's date)
    date_str = datetime.now().strftime('%Y-%m-%d')
    
    # 6. Write to File
    try:
        with open(DATA_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([date_str, trans_type, amount, category, description])
        print("\n✅ Transaction successfully recorded!")
    except Exception as e:
        print(f"\n❌ ERROR: Could not write to file: {e}")

def view_transactions():
    """Reads and displays all transactions from the CSV file."""
    print("\n--- ALL TRANSACTIONS ---")
    try:
        with open(DATA_FILE, 'r', newline='') as f:
            reader = csv.reader(f)
            # Use next() with a default value to handle empty files gracefully
            try:
                header = next(reader)
            except StopIteration:
                print("No transactions recorded yet.")
                return
            
            # Print header with simple formatting
            print(f"{header[0]:<12}{header[1]:<6}{header[2]:>10}{header[3]:<18}{header[4]:<40}")
            print("-" * 86)
            
            # Print each transaction
            has_data = False
            for row in reader:
                # Format type and amount
                trans_type_display = "INCOME" if row[1] == 'I' else "EXPENSE"
                # Ensure float conversion for formatting
                try:
                    amount_display = f"{float(row[2]):,.2f}"
                except ValueError:
                    amount_display = "N/A" # Handle non-numeric amount gracefully
                
                print(f"{row[0]:<12}{trans_type_display:<6}{amount_display:>10}{row[3]:<18}{row[4]:<40}")
                has_data = True
            
            if not has_data:
                print("No transactions recorded yet.")
                
    except FileNotFoundError:
        print("Data file not found. Please add a transaction first.")
    except Exception as e:
        print(f"❌ ERROR: Could not read transactions: {e}")


def generate_summary():
    """Calculates and displays total income, total expense, and net balance."""
    total_income = 0.0
    total_expense = 0.0

    print("\n--- FINANCIAL SUMMARY ---")
    try:
        with open(DATA_FILE, 'r', newline='') as f:
            reader = csv.reader(f)
            
            # Use next() with a default value to handle empty files gracefully
            try:
                next(reader) # Skip header row
            except StopIteration:
                print("No transactions recorded to generate a summary.")
                return

            has_data = False
            for row in reader:
                has_data = True
                try:
                    # Row structure: [Date, Type, Amount, Category, Description]
                    trans_type = row[1]
                    amount = float(row[2])

                    if trans_type == 'I':
                        total_income += amount
                    elif trans_type == 'E':
                        total_expense += amount
                except (ValueError, IndexError):
                    # Skip malformed row without stopping the entire summary
                    continue

            if not has_data:
                print("No transactions recorded to generate a summary.")
                return

            net_balance = total_income - total_expense

            print(f"Total Income:     ${total_income:,.2f}")
            print(f"Total Expense:   ${total_expense:,.2f}")
            print("-" * 30)
            
            # Display net balance with appropriate color/sign logic
            sign = ""
            if net_balance > 0:
                sign = " (Surplus)"
            elif net_balance < 0:
                sign = " (Deficit)"

            print(f"Net Balance:     ${net_balance:,.2f}{sign}")

    except FileNotFoundError:
        print("Data file not found. Please add a transaction first.")
    except Exception as e:
        print(f"❌ ERROR: Could not read transactions for summary: {e}")

def main():
    """Main function to run the command-line interface."""
    ensure_data_file()

    while True:
        print("\n==================================")
        print("PERSONAL FINANCE TRACKER (FRESHER)")
        print("==================================")
        print("1. Add New Transaction")
        print("2. View All Transactions")
        print("3. Generate Summary (Income/Expense/Balance)")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            generate_summary()
        elif choice == '4':
            print("\nThank you for using the Finance Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == '__main__':
    main()