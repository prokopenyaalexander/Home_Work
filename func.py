from DatabaseCreation import *

"""
add record
"""


def add(n, p, q, c):
    ins = products.insert().values(name=n, price=p, quantity=q, comments=c)
    result = conn.execute(ins)


"""
read record
"""


def read():
    records = products.select()
    result = conn.execute(products.select()).fetchall()
    print(result)


"""
update record by ID
"""


def update(n, p, q, c, number_of_record):
    # table.update().where(conditions).values(SET expressions)
    if number_of_record > 0:
        upt = products.update().where(products.c.id == number_of_record).values(name=n, price=p, quantity=q, comments=c)
    result = conn.execute(upt)


"""
delete record by ID
"""


def delete(number_of_id):
    if number_of_id == 0:
        products.delete()
    else:
        delete_item = products.delete().where(products.c.id == number_of_id)
        result = conn.execute(delete_item)
