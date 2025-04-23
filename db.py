import csv
import psycopg2
from psycopg2 import sql

# Connect to your postgres DB
conn = psycopg2.connect(
    host="localhost",      
    database="my_database", 
    user="postgres",       
    password="pxn4life!",
    port="5432",           
    sslmode="disable"      
)
# Open a cursor to perform database operations
cur = conn.cursor()

# Create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        phone VARCHAR(50)
    )
""")

# Commit changes
conn.commit()

def insert_data(first_name, last_name, phone):
    cur.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)", (first_name, last_name, phone))
    conn.commit()

def upload_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            insert_data(row[0], row[1], row[2])

def enter_data():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone: ")
    insert_data(first_name, last_name, phone)

def update_data(id, first_name=None, phone=None):
    if first_name:
        cur.execute("UPDATE phonebook SET first_name = %s WHERE id = %s", (first_name, id))
    if phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE id = %s", (phone, id))
    conn.commit()

def query_data(filter=None):
    if filter:
        query = sql.SQL("SELECT * FROM phonebook WHERE {}").format(sql.SQL(filter))
        cur.execute(query)
    else:
        cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_data(id):
    cur.execute("DELETE FROM phonebook WHERE id = %s", (id,))
    conn.commit()


def get_records_by_pattern(pattern):
    cur.execute("SELECT * FROM phonebook WHERE first_name LIKE %s OR last_name LIKE %s OR phone LIKE %s", (f'%{pattern}%', f'%{pattern}%', f'%{pattern}%'))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def insert_or_update_user(first_name, last_name, phone):
    try:
        cur.execute("SELECT * FROM phonebook WHERE first_name = %s AND last_name = %s", (first_name, last_name))
        if cur.fetchone() is None:
            cur.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)", (first_name, last_name, phone))
        else:
            cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s AND last_name = %s", (phone, first_name, last_name))
        conn.commit()
    except Exception as e:
        print(f"Error inserting/updating user: {e}")

def insert_many_users(user_list):
    for user in user_list:
        first_name, last_name, phone = user
        if len(phone) == 10:  # Check if phone number is correct
            insert_or_update_user(first_name, last_name, phone)
        else:
            print(f"Incorrect data: {user}")

def query_data_with_pagination(limit, offset):
    cur.execute("SELECT * FROM phonebook LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_data_by_username_or_phone(username=None, phone=None):
    if username:
        cur.execute("DELETE FROM phonebook WHERE first_name = %s OR last_name = %s", (username, username))
    if phone:
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()


if __name__ == "__main__":
    while True:
        print("\nPhonebook Menu:")
        print("1. Insert new contact")
        print("2. Upload from CSV")
        print("3. Update contact")
        print("4. Show all contacts")
        print("5. Search by pattern")
        print("6. Insert or update contact")
        print("7. Bulk insert with check")
        print("8. Paginated query")
        print("9. Delete by ID")
        print("10. Delete by name or phone")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            enter_data()
        elif choice == "2":
            path = input("Enter CSV file path: ")
            upload_csv(path)
        elif choice == "3":
            id = int(input("Enter ID to update: "))
            fname = input("New first name (leave blank to skip): ")
            phone = input("New phone (leave blank to skip): ")
            update_data(id, fname if fname else None, phone if phone else None)
        elif choice == "4":
            query_data()
        elif choice == "5":
            pattern = input("Enter search pattern: ")
            get_records_by_pattern(pattern)
        elif choice == "6":
            fn = input("First name: ")
            ln = input("Last name: ")
            ph = input("Phone: ")
            insert_or_update_user(fn, ln, ph)
        elif choice == "7":
            n = int(input("How many users to insert? "))
            users = []
            for _ in range(n):
                fn = input("First name: ")
                ln = input("Last name: ")
                ph = input("Phone: ")
                users.append((fn, ln, ph))
            insert_many_users(users)
        elif choice == "8":
            limit = int(input("Limit: "))
            offset = int(input("Offset: "))
            query_data_with_pagination(limit, offset)
        elif choice == "9":
            id = int(input("Enter ID to delete: "))
            delete_data(id)
        elif choice == "10":
            name = input("Enter name to delete (leave blank to skip): ")
            phone = input("Enter phone to delete (leave blank to skip): ")
            delete_data_by_username_or_phone(name if name else None, phone if phone else None)
        elif choice == "0":
            break
        else:
            print("Invalid option. Try again.")
