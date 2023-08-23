#!/usr/bin/python3
from sqlalchemy import create_engine
engine = create_engine("mysql://root:root@localhost:3306/hbtn_0e_4_usa")
# conn = engine.connect()
# dbapi_raw_conn = conn.connection
dbapi = engine.raw_connection()
dbapi_cursor = dbapi.cursor()
dbapi_cursor.execute("SELECT * FROM states;")
results = dbapi_cursor.fetchall()
for result in results:
    print(result)
results.close()
