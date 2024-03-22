#!/usr/bin/python3
# script lists all cities from the database hbtn_0e_4_usa
"""lists all cities from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM cities AS c \
                JOIN states AS s ON c.state_id=s.id ORDER BY c.id ASC")
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    conn.close()
