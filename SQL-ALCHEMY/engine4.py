#!/usr/bin/python3
from sqlalchemy import create_engine
engine = create_engine("mysql://root:root@localhost:3306/hbtn_0e_4_usa")
conn = engine.connect()
trans = conn.begin()
result = conn.execute("SELECT * FROM states where states.name = 'Nevada';")
results = conn.execute("SELECT * FROM states ORDER BY states.name ASC;")
for row in result:
    print(row, end="\n\n")
for rows in results:
    print(rows)
trans.close()
