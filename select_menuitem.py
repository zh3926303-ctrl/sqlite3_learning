import sqlite3
def select(conn):
    result = conn.execute("SELECT * FROM menu_itemsschema")
    for data in result:
        print(data)