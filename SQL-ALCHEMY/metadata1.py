#!/usr/bin/python3
from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String
from sqlalchemy import create_engine, ForeignKey


metadata = MetaData()
user_table = Table("users",
                   metadata,
                   Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
                   Column("name", String(256), nullable=False),
                   Column("age", Integer, nullable=False)
                   )
engine = create_engine("mysql://root:root@localhost:3306/hbtn_0e_4_usa")
metadata.create_all(engine)
address_table = Table("address",
                      metadata,
                      Column("id", Integer, primary_key=True, nullable=False, autoincrement=True),
                      Column("email_address", String(50), nullable=False),
                      Column("user_id", Integer, ForeignKey("users.id"))
                      )
address_table.create(engine)
