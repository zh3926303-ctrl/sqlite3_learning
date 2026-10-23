import pos_schema
import insert_categories
import insert_categories
import insert_products
import insert_customerss
import insert_employees
import insert_sales
import insert_saleitems


connection = pos_schema.schema()
insert_categories.insert(connection)
insert_products.insert(connection)
insert_customerss.insert(connection)
insert_employees.insert(connection)
insert_sales.insert(connection)
insert_saleitems.insert(connection)