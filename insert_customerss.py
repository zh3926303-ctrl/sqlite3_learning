import sqlite3
def insert(conn):
    conn.executemany(
        "INSERT INTO customers(id,name,email) VALUES(?,?,?)",
        [
            (1,"Ana","ana@example.com"),
            (2,"Ben","ben@example.com"),
            (3,"Cara","cara@example.com")
        ]
    )
    conn.commit()