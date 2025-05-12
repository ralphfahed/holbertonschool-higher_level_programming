#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
It takes 3 arguments: MySQL username, password, and database name.
The script connects to a local MySQL server and retrieves all records
from the 'states' table, sorted by id in ascending order.
"""

import MySQLdb
import sys


def list_states():
    """Connects to the database and lists all states sorted by id ASC"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    try:
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
    cur.execute("SELECT * FROM states ORDER BY id ASC")

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
    list_states()

