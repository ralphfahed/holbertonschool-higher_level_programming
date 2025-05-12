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
    # Fetching the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Establish the connection to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor to interact with the database
    cur = db.cursor()

    # Query to select states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows from the executed query
    rows = cur.fetchall()

    # Print each row (state)
    for row in rows:
        print(row)

    # Clean up by closing the cursor and the database connection
    cur.close()
    db.close()

if __name__ == "__main__":
    list_states()

