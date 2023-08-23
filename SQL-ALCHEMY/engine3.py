#!/usr/bin/python3
from sqlalchemy import create_engine
engine = create_engine("mysql://root:root@localhost:3306/hbtn_0e_4_usa")
# conn = engine.connect()
# dbapi_raw_conn = conn.connection
dbapi = engine.raw_connection()
dbapi_cursor = dbapi.cursor()
dbapi_cursor.execute("SELECT * FROM states;")
result = dbapi_cursor.fetchone()
print(result)
result.close()
