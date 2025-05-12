#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa where the name matches the argument.
It takes 4 arguments: MySQL username, password, database name, and state name.
The script connects to a local MySQL server and retrieves matching records from the 'states' table,
sorted by id in ascending order. It uses parameterized queries to prevent SQL injection.
"""

import MySQLdb
import sys

def search_states():
    """
    Connects to the database and lists all states matching the state name, sorted by id in ascending order.
    Uses parameterized queries to prevent SQL injection.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search_name = sys.argv[4]  # The state name to search for

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create cursor and execute parameterized query to search for the exact state name
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (search_name,))  # The parameter is passed safely using tuple

    # Fetch and print results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()

if __name__ == "__main__":
    search_states()

