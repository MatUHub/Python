import sqlite3

def create_db():
    base = sqlite3.connect('new db')
    base.close()

def create_table():
    base = sqlite3.connect('new db')
    base.execute("""CREATE TABLE IF NOT EXISTS cars (name text,
                                                     year_of_manufacture text, 
                                                     mileage text, 
                                                     color text, 
                                                     engine_power text, 
                                                     drive text)""")
    base.commit()
    base.execute("""CREATE TABLE IF NOT EXISTS sports_cars (name text,
                                                     year_of_manufacture text, 
                                                     mileage text, 
                                                     color text, 
                                                     engine_power text, 
                                                     drive text)""")
    base.commit()
    base.execute("""CREATE TABLE IF NOT EXISTS trucks (name text,
                                                     year_of_manufacture text, 
                                                     mileage text, 
                                                     color text, 
                                                     engine_power text, 
                                                     drive text)""")
    base.commit()
    base.close()

def add_data_to_table(table, name, year_of_manufacture, mileage, color, engine_power, drive):
    base = sqlite3.connect('new db')
    cursor = base.cursor()
    cursor.execute(f"""INSERT INTO {table} VALUES('{name}',{year_of_manufacture},{mileage},'{color}',{engine_power},'{drive}')""")
    base.commit()
    base.close()
    print("Данные добавлены!")

def show_data(table):
    base = sqlite3.connect('new db')
    cursor = base.cursor()
    a = cursor.execute(f"""SELECT * FROM {table}""").fetchall()
    for i in a:
        print(i)
    base.close()

def find_data_value(table, column, value):
    base = sqlite3.connect('new db')
    cursor = base.cursor()
    a = cursor.execute(f"""SELECT * FROM {table} WHERE {column} == '{value}'""").fetchall()
    for i in a:
        print(i)
    base.close()

def data_update(table, calum1, value1, value2):
    base = sqlite3.connect('new db')
    cursor = base.cursor()
    cursor.execute(f"""UPDATE {table} SET {calum1} == '{value1}' WHERE name == '{value2}' """)
    base.commit()
    base.close()
    print("Данные изменены!")

def delete_data(table, name):
    base = sqlite3.connect('new db')
    cursor = base.cursor()
    cursor.execute(f"""DELETE FROM {table} WHERE name == '{name}'""")
    base.commit()
    base.close()
    print("Данные удалены!")



