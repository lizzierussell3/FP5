import sqlite3
import os

# --- Configuration ---
# You MUST change the database file name and table name
# to match what your 'fp5.py' file is actually using.
DATABASE_FILE = "customer_data.db"  # 👈 **CHANGE THIS**
TABLE_NAME = "customers"            # 👈 **CHANGE THIS**

def view_customer_data():
    """
    Connects to the SQLite database and prints all customer records.
    """
    if not os.path.exists(DATABASE_FILE):
        print(f"🛑 Error: Database file '{DATABASE_FILE}' not found.")
        print("Ensure this script is in the same directory as the database file.")
        return

    conn = None
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        print(f"✅ Successfully connected to database: {DATABASE_FILE}")
        
        # 1. Get column names for a header
        cursor.execute(f"SELECT * FROM {TABLE_NAME} LIMIT 1")
        column_names = [description[0] for description in cursor.description]
        
        # 2. Get all rows
        cursor.execute(f"SELECT * FROM {TABLE_NAME}")
        rows = cursor.fetchall()
        
        if not rows:
            print(f"\nℹ️ No data found in the table '{TABLE_NAME}'.")
            return

        # 3. Print the data
        print("\n--- Customer Data ---")
        
        # Print header
        header = " | ".join(column_names)
        print(header)
        print("-" * len(header.replace("|", "---"))) # Separator line
        
        # Print rows
        for row in rows:
            # Convert all elements to string and join
            print(" | ".join(map(str, row)))
            
    except sqlite3.OperationalError as e:
        print(f"\n❌ Database Operational Error: {e}")
        print(f"   Did you verify the table name '{TABLE_NAME}' is correct?")
        print(f"   If you're using a different database technology (like MySQL, PostgreSQL, etc.), this script won't work.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    finally:
        # Close the connection
        if conn:
            conn.close()
            print("\nConnection closed.")

if __name__ == "__main__":
    view_customer_data()