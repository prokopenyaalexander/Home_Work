from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData

engine = create_engine('sqlite:///shop.db', echo=True)

meta = MetaData()

products = Table(
    'products', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('price', String),
    Column('quantity', String),
    Column('comments', String),
)
meta.create_all(engine)
conn = engine.connect()



