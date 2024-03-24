import sqlite3


# Function to create the database tables
def create_tables():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Create users table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT)"""
    )

    # Create customers table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS customers
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    phone TEXT,
                    email TEXT,
                    address TEXT)"""
    )

    # Create invoices table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS invoices
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    date TEXT,
                    amount REAL,
                    status TEXT)"""
    )

    conn.commit()
    conn.close()


# Function to add a new user to the database
def add_user(username, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)", (username, password)
    )

    conn.commit()
    conn.close()


# Function to retrieve a user by username
def get_user_by_username(username):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    conn.close()
    return user


def add_customer(name, phone, email, address):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO customers (name, phone, email, address) VALUES (?, ?, ?, ?)",
        (name, phone, email, address),
    )
    conn.commit()
    conn.close()


def edit_customer(id, name, phone, email, address):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE customers SET name=?, phone=?, email=?, address=? WHERE id=?",
        (name, phone, email, address, id),
    )
    conn.commit()
    conn.close()


def add_invoice(name, date, amount, status):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO invoices (name, date, amount, status) VALUES (?, ?, ?, ?)",
        (name, date, amount, status),
    )
    conn.commit()
    conn.close()


def edit_invoice(id, name, date, amount, status):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE invoices SET name=?, date=?, amount=?, status=? WHERE id=?",
        (name, date, amount, status, id),
    )
    conn.commit()
    conn.close()


def getCustomers():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * from customers")
    data = cursor.fetchall()
    data = [list(d) for d in data]

    conn.commit()
    conn.close()
    return data


def getCustomerById(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(f"SELECT * from customers where id={id}")
    data = cursor.fetchone()
    data = [d for d in data]

    conn.commit()
    conn.close()
    return data


def getInvoices():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * from invoices")
    data = cursor.fetchall()
    data = [list(d) for d in data]
    conn.commit()
    conn.close()
    return data


def getInvoiceById(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(f"SELECT * from invoices where id={id}")
    data = cursor.fetchone()
    data = [d for d in data]
    conn.commit()
    conn.close()
    return data


# Example usage:
if __name__ == "__main__":
    # create_tables()
    # # Add users to the database
    # add_user("admin", "password")
    # add_user("user1", "password123")

    # add_customer("John Doe", "123-456-7890", "john@example.com", "123 Main St")
    # add_customer("Jane Smith", "987-654-3210", "jane@example.com", "456 Oak Ave")
    # add_invoice("John Doe", "2024-03-23", 100.00, "Paid")
    # add_invoice("Jane Smith", "2024-03-24", 150.00, "Unpaid")
    # # Retrieve a user by username
    print(getInvoices())
    # print("User:", user)
