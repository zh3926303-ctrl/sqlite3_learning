import sqlite3
def insert(conn):
    conn.executemany(
        "INSERT INTO employees(id,name,role) VALUES(?,?,?)",
        [
            (1,"Mya Mya","Cashier"),
            (2,"Leo","Manager"),
            (3,"Nina","Cashier")
        ]
    )
    conn.commit()