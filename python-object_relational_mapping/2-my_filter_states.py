#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


def filter_states():
    """Displays all values in states table where name matches the argument"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )

        # Create cursor and execute query
        cur = db.cursor()
        query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
        cur.execute(query)

        # Fetch and print results
        rows = cur.fetchall()
        for row in rows:
            print(row)

  # Clean up
    cur.close()
    db.close()

if __name__ == "__main__":
    filter_states()
