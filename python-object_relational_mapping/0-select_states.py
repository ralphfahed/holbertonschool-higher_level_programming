#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":

    # Connect to MySQL server
    def list_states():
    """Connects to the database and lists all states sorted by id ASC"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

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

     # Clean up
    cur.close()
    db.close()
