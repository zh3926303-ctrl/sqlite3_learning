import sqlite3
def insert(conn):
    conn.executemany(
        "INSERT INTO order_itemsschema(order_item_id,order_id,item_id,quantity,unit_price) VALUES(?,?,?,?,?)",
        [
            (1,1,1,3,2500),
            (2,2,2,4,3500)
        ]
    )
    conn.commit()
    print("insert orderitem")