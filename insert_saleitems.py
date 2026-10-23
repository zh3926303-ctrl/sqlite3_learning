import sqlite3
def insert(conn):
    conn.executemany(
        "INSERT INTO sale_items(id,sale_id,product_id,qty,unit_cents) VALUES(?,?,?,?,?)",
        [
            (1,1001,1,2,350),
            (2,1001,2,1,220),
            (3,1002,3,2,250),
            (4,1003,4,1,450),
            (5,1003,5,2,100)
        ]
    )
    conn.commit()