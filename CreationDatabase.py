from sqlalchemy import *

engine = create_engine('sqlite:///car.db', echo=True)

meta = MetaData()

Brand = Table(
    'Brand', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
)

Car = Table(
    'Car', meta,
    Column('id', Integer, primary_key=True),
    Column('model', String),
    Column('release_year', String),
    Column('brand', String, ForeignKey('Brand.id')),
)

meta.create_all(engine)
conn = engine.connect()
