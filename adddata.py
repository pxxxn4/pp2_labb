import csv
import psycopg2

conn = psycopg2.connect(
    host="localhost",      
    database="my_database", 
    user="postgres",       
    password="pxn4life!",
    port="5432",           
    sslmode="disable"      
)

cur = conn.cursor()

# Создаем таблицу phonebook, если она не существует
cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        phone VARCHAR(50)
    )
""")
conn.commit()

def insert_data(first_name, last_name, phone):
    cur.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)", (first_name, last_name, phone))
    conn.commit()

def upload_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            parserRow = row[0].split(";")
            insert_data(parserRow[0], parserRow[1], parserRow[2])

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

def query_data():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No data found")

def delete_data(id):
    cur.execute("DELETE FROM phonebook WHERE id = %s", (id,))
    conn.commit()

upload_csv('/Users/pxn4/Documents/numbers2.csv')


query_data()

# Закрытие соединения
cur.close()
conn.close()
