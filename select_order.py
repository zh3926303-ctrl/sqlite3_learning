import sqlite3 
def select(conn):
    result = conn.execute("SELECT order_date FROM ordersschema")
    for data in result:
        print(data)