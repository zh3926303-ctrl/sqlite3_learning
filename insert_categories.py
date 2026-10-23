import sqlite3 
def insert(conn):
    conn.executemany(
        "INSERT INTO categories(id,names) VALUES(?,?)",
        [
        (1,"Drinks"),
        (2,"Food"),
        (3,"Stationery")
        ]
    )
    conn.commit()