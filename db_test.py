import sqlite3

# Function to connect to the database
def connect_to_db(db_name):
    try:
        conn = sqlite3.connect(db_name)
        print(f"Connected to database: {db_name}")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Function to insert sample data
def insert_sample_data(cursor):
    try:
        cursor.execute("INSERT OR IGNORE INTO Customers (customerID, name, email, phone, signupDate) VALUES (1, 'John Doe', 'john@example.com', '1234567890', '2025-01-01')")
        cursor.execute("INSERT OR IGNORE INTO Products (productID, name, description, price, cost, category) VALUES (1, 'Product A', 'Description A', 100.00, 50.00, 'Category A')")
        cursor.execute("INSERT OR IGNORE INTO SalesTransactions (transactionID, customerID, productID, transactionDate, quantity, price) VALUES (1, 1, 1, '2025-04-01', 2, 200.00)")
        print("Sample data inserted successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred while inserting sample data: {e}")

# Function to fetch and display data
def fetch_data(cursor):
    try:
        # Fetch table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print("\nTables in the database:")
        for table in tables:
            print(table[0])

        # Fetch data from SalesTransactions
        cursor.execute("SELECT * FROM SalesTransactions;")
        rows = cursor.fetchall()
        print("\nData in SalesTransactions table:")
        if rows:
            for row in rows:
                print(row)
        else:
            print("No data found in SalesTransactions table.")
    except sqlite3.Error as e:
        print(f"An error occurred while fetching data: {e}")

# Main function
def main():
    db_name = "database.db"
    
    # Connect to the database using a context manager
    with connect_to_db(db_name) as conn:
        if conn is None:
            return
        
        cursor = conn.cursor()
        
        # Insert sample data and fetch data
        insert_sample_data(cursor)
        
        # Commit changes to make them permanent
        conn.commit()
        
        fetch_data(cursor)

# Entry point of the script
if __name__ == "__main__":
    main()