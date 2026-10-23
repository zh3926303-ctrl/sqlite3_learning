import sqlite3 

def schema():
    conn = sqlite3.connect("restaurant_manage.db")
    print("Connected")

    customersschema = """
    CREATE TABLE IF NOT EXISTS customers(
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL
    )
    """
    conn.execute(customersschema)


    ordersschema = """
    CREATE TABLE IF NOT EXISTS ordersschema(
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    table_number INTEGER NOT NULL,   
    order_date TEXT NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customers_id)
    )
    """
    conn.execute(ordersschema)


    order_itemsschema = """
    CREATE TABLE IF NOT EXISTS order_itemsschema(
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price REAL,
    FOREIGN KEY (order_id) REFERENCES ordersschema(order_id)
    )
    """
    conn.execute(order_itemsschema)

    menu_itemsschema = """
    CREATE TABLE IF NOT EXISTS menu_itemsschema(
    item_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL,
    is_available INTEGER,
    FOREIGN KEY (item_id) REFERENCES order_itemsschema(item_id)
    )
    """
    conn.execute(menu_itemsschema)

    return conn


