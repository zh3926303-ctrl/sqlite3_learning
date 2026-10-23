import sqlite3 

def insert(conn):
    conn.executemany(
        "INSERT INTO customers(customer_id,name,phone,address) VALUES(?,?,?,?)",
        [
            (1,"Mg Mg","0912345678","Yangon"),
            (2,"Zaw Zaw","0987654321","Mandalay")
            
        ]
    )
    conn.commit()
    print("insert customers")