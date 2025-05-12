#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa whose names start with 'N'.
It takes 3 arguments: MySQL username, password, and database name.
The script connects to a local MySQL server and retrieves all records from the 'states' table
where the name starts with 'N', sorted by id in ascending order.
"""

import MySQLdb
import sys

def list_states():
    """Connects to the database and lists all states starting with 'N' sorted by id ASC"""
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

    # Create cursor and execute query to filter states starting with 'N'
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch and print results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()

if __name__ == "__main__":
    list_states()

