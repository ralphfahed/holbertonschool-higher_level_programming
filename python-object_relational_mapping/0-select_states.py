#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa,
sorted by states.id in ascending order.
"""

import MySQLdb
import sys


def list_states():
    """
    Connects to a MySQL database and prints all states
    from the 'states' table ordered by id ascending.
    """
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    list_states()

