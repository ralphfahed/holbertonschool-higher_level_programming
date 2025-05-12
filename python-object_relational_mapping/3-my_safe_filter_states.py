#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument, safe from MySQL injection.
"""

import MySQLdb
import sys


def safe_filter_states():
    """Displays all values in states table where name matches the argument safely"""

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )

        # Create cursor and execute query using parameterized query
        cur = db.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cur.execute(query, (state_name,))

        # Fetch and print results
        rows = cur.fetchall()
        for row in rows:
            print(row)

    finally:
        # Clean up
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    safe_filter_states()
