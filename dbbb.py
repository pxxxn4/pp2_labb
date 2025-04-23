import csv
import psycopg2
from psycopg2 import sql

print("Connecting to the database...")
conn = psycopg2.connect(
    host="localhost",      
    database="my_database", 
    user="postgres",       
    password="pxn4life!",
    port="5432",           
    sslmode="disable"      
)
print("Connection successful!")
cur = conn.cursor()

# Создание таблицы, если она не существует
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
        next(reader)  # пропустить заголовок
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
        # Простое использование строки как условия для фильтрации
        query = f"SELECT * FROM phonebook WHERE {filter}"
        cur.execute(query)
    else:
        cur.execute("SELECT * FROM phonebook")
    
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_data(id):
    cur.execute("DELETE FROM phonebook WHERE id = %s", (id,))
    conn.commit()

# Пример добавления данных
insert_data("Pupa", "Lupa", "123-456-7890")
print("Data inserted!")


# Закрыть соединение, когда все операции завершены
conn.close()
