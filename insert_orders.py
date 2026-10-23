import sqlite3

def insert(conn):
    conn.executemany(
        "INSERT INTO ordersschema(order_id,customer_id,table_number,order_date,status) VALUES(?,?,?,?,?)",
        [
            (1,1,1,"15-10-2026","completed"),
            (2,2,2,"16-10-2026","pending")
        ]
    )
    conn.commit()
    print("insert orders")
