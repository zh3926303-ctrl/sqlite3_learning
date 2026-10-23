import sqlite3
def insert(conn):
    conn.executemany(
        "INSERT INTO sales(id,customer_id,employee_id,sale_date,total_cents) VALUES(?,?,?,?,?)",
        [
            (1001,1,1,2026-10-20,920),
            (1002,2,2,2026-10-20,500),
            (1003,3,1,2026-10-20,650)
        ]
    )
    conn.commit()