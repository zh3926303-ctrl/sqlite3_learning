import sqlite3 
def select(conn):
    result = conn.execute("SELECT address FROM customers")
    for data in result:
        print(data)