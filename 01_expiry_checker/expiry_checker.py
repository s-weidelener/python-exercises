import sqlite3
import datetime

# Connection and setup
conn = sqlite3.connect('mein_projekt.db')
today = datetime.date.today()
cursor = conn.cursor()

# Database structure
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        barcode TEXT,
        name TEXT NOT NULL,
        expiry_date DATE,
        add_at DATE,
        price REAL
    )
''')

# Insert example data 
cursor.execute("INSERT INTO products (name, expiry_date) VALUES (?, ?)", ("Bread", "2026-02-10"))
conn.commit()

def check_expired():
    expiry_date = cursor.execute("SELECT name, expiry_date FROM products")
    products = cursor.fetchall()
   
    for name, expiry_date in products:
        print(f"{expiry_date}")
        if not expiry_date:
            print(f"Product {name} has no date")
            continue
        expiry_date_obj = datetime.datetime.strptime(expiry_date, "%Y-%m-%d").date()
        days_until_expiry = (expiry_date_obj - today).days
        if 0 <= days_until_expiry <= 3: 
            print(f"{name} expires in {days_until_expiry} days")
        elif days_until_expiry < 0:
            print(f"{name} has already expired")

check_expired()

