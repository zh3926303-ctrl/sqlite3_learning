import sqlite3 
def insert(conn):
    conn.executemany(
        "INSERT INTO menu_itemsschema(item_id,name,category,price,is_available) VALUES(?,?,?,?,?)",
        [
            (1,"coffee","drink",1500,1),
            (2,"tea","drink",2000,2)
        
        ]
    )
    conn.commit()
    print("insert menu_item")