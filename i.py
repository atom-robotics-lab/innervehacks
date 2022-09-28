from xmlrpc.client import DateTime
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///test.db', echo = True)
meta = MetaData()

Model = Table(
   'Model', meta, 
   Column('id', Integer, primary_key = True), 
   Column('firstname', String(200),nullable=False), 
   Column('address', String(200),nullable=False)
)
meta.create_all(engine)