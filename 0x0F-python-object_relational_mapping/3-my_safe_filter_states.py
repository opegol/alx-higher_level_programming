#!/usr/bin/python3
# script takes in an argument and displays all values in the states table
# of hbtn_0e_0_usa where name matches the arg safely to avoid sql injection
"""SQL injection safe script that displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s \
                ORDER BY id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    conn.close()
