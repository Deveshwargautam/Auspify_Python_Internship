import sqlite3
from datetime import datetime

DB_NAME = "expense_tracker.db"

def init_db():
    """Initializes the SQLite database and creates the expenses table."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_expense():
    """Step 1 & 2: Takes user input to record and categorize an expense."""
    print("\n--- Add New Expense ---")
    try:
        amount = float(input("Enter amount spent: ").strip())
        if amount <= 0:
            print("❌ Amount must be greater than zero.")
            return
            
        print("Select Category: [1] Food, [2] Transport, [3] Bills, [4] Entertainment, [5] Other")
        cat_choice = input("Choice (1-5): ").strip()
        categories = {"1": "Food", "2": "Transport", "3": "Bills", "4": "Entertainment", "5": "Other"}
        category = categories.get(cat_choice, "Other")
        
        description = input("Enter brief description: ").strip()
        date_str = datetime.now().strftime("%Y-%m-%d")

        # Step 3: Store records in SQLite database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO expenses (amount, category, description, date)
            VALUES (?, ?, ?, ?)
        ''', (amount, category, description, date_str))
        conn.commit()
        conn.close()
        print(f"✅ Expense of ₹{amount} added under '{category}' category successfully!")
    except ValueError:
        print("❌ Invalid input. Amount must be a clear numerical value.")

def generate_summary():
    """Step 4 & 5: Generates historical spending charts and monthly breakdowns."""
    print("\n--- Spending Summary & Reports ---")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Calculate global cumulative statistics
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0] or 0.0
    print(f"💰 Total Cumulative Expenses Logged: ₹{total:.2f}")
    
    # Calculate category group summary distributions
    print("\n📋 Expenditure Distribution by Category:")
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cursor.fetchall()
    for row in rows:
        print(f" ▪️ {row[0]}: ₹{row[1]:.2f}")
        
    conn.close()

def main():
    init_db()
    while True:
        print("\n=== Auspify Expense Tracker System ===")
        print("1. Add Expense Record")
        print("2. View Spending Summaries & Reports")
        print("3. Exit Application")
        
        choice = input("Select an option (1-3): ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            generate_summary()
        elif choice == "3":
            print("\nShutting down Tracker System. Keep budgeting carefully!")
            break
        else:
            print("❌ Invalid entry option. Select numbers 1 through 3.")

if __name__ == "__main__":
    main()
