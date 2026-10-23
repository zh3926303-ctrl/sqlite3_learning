import schema
import schema
import insert_customers
import insert_orders
import insert_orderitem
import insert_menuitem
import select_customer
import select_orderitem
import select_order
import select_menuitem

connection = schema.schema()

insert_customers.insert(connection)
insert_orders.insert(connection)
insert_orderitem.insert(connection)
insert_menuitem.insert(connection)
select_customer.select(connection)
select_orderitem.select(connection)
select_order.select(connection)
select_menuitem.select(connection)