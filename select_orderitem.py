import sqlite3
def select(conn):
    result = conn.execute("SELECT unit_price FROM order_itemsschema ")
    for data in result:
        print(data)