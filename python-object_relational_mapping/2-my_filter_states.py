#!/usr/bin/python3
"""
This script filters states from the database hbtn_0e_0_usa.
It takes 4 arguments: MySQL username, password, database name, and state name to search for.
The script connects to a local MySQL server and retrieves all states with a name matching the search name,
sorted by id in ascending order.
"""

import MySQLdb
import sys

def filter_states():
    """Connects to the database and filters states based on user input, sorted by id ASC."""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]  # The state name to search for

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create cursor and execute query to search for states matching the state_name
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

