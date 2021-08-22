from CreationDatabase import *

"""
add record
"""


def add(m, r, b):
    ins = Car.insert().values(model=m, release_year=r, brand=b)
    conn.execute(ins)


"""
read record
"""


def read():
    Car.select()
    result = conn.execute(Car.select()).fetchall()
    print(result)


"""
update record by ID
"""


def update(m, r, b, number_of_record):
    # table.update().where(conditions).values(SET expressions)
    if number_of_record > 0:
        upt = Car.update().where(Car.c.id == number_of_record).values(model=m, release_year=r, brand=b)
    result = conn.execute(upt)


"""
delete record by ID
"""


def delete(number_of_id):
    if number_of_id == 0:
        Car.delete()
    else:
        delete_item = Car.delete().where(Car.c.id == number_of_id)
        result = conn.execute(delete_item)


def add_two(n):
    ins = Brand.insert().values(name=n)
    result = conn.execute(ins)

###############
def add_two(n):
    ins = Brand.insert().values(name=n)
    conn.execute(ins)


"""
read record
"""


def read_two():
    Brand.select()
    result = conn.execute(Brand.select()).fetchall()
    print(result)


"""
update record by ID
"""


def update_two(n, number_of_record):
    if number_of_record > 0:
        upt = Brand.update().where(Brand.c.id == number_of_record).values(name=n)
    conn.execute(upt)


"""
delete record by ID
"""


def delete_two(number_of_id):
    if number_of_id == 0:
        Brand.delete()
    else:
        delete_item = Brand.delete().where(Brand.c.id == number_of_id)
        conn.execute(delete_item)


