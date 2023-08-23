#!/usr/bin/python3
from sqlalchemy import create_engine
engine = create_engine("mysql://root:root@localhost:3306/hbtn_0e_4_usa")
"""
with engine.connect() as conn:
    rows = conn.execute("SELECT cities.name FROM cities
                  JOIN states ON states.id = cities.state_id
                  WHERE states.name = 'Texas'
                  ORDER BY cities.name ASC;")
    for row in rows:
        print(row)
"""
results = engine.execute("""SELECT c.name FROM
                          cities AS c JOIN states AS s
                          ON s.id = c.state_id WHERE
                          s.name = %s ORDER BY c.name ASC;""",
                          "Texas")
for result in results:
    print(result[0].split(",")[0], end=" ")
results.close()
