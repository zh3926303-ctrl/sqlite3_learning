import sqlite3

def schema():
    conn = sqlite3.connect("pos.db")
    print("Connected")

    categoriesschema = """
    CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY,
    names TEXT NOT NULL
    )
    """
    conn.execute(categoriesschema)

    productsschema = """
    CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    price_cents INTEGER NOT NULL,
    stock INTEGER NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
    )
    """
    conn.execute(productsschema)

    customersschema = """
    CREATE TABLE IF NOT EXISTS customers(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL
    )
    """
    conn.execute(customersschema)

    employeesschema = """
    CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    role TEXT NOT NULL
    )
    """
    conn.execute(employeesschema)

    salesschema = """
    CREATE TABLE IF NOT EXISTS sales(
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    sale_date INTEGER NOT NULL,
    total_cents INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
    FOREIGN KEY (employee_id) REFERENCES emplpyees(id)
    )
    """
    conn.execute(salesschema)

    sale_itemsschema = """
    CREATE TABLE IF NOT EXISTS sale_items(
    id INTEGER PRIMARY KEY,
    sale_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    qty INTEGER NOT NULL,
    unit_cents INTEGER NOT NULL,
    FOREIGN KEY (sale_id) REFERENCES sales(id)
    FOREIGN KEY (product_id) REFERENCES products(id)
    )
    """
    conn.execute(sale_itemsschema)

    return conn