#!/usr/bin/python3
# script takes in the name of a state as an argument and lists
# all cities of that state, using the database hbtn_0e_4_usa
"""Script takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT c.name FROM cities AS c \
                JOIN states AS s ON c.state_id=s.id \
                WHERE s.name=%s ORDER BY c.id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    if rows:
        for r in rows[:-1]:
            print(r[0], end=', ')
        print(rows[-1][0])
    else:
        print('')
    cur.close()
    conn.close()
