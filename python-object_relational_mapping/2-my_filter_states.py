#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
It takes 4 arguments: MySQL username, password, database name, and state name.
The script connects to a local MySQL server and retrieves all records
from the 'states' table, sorted by id in ascending order.
"""
import MySQLdb
import sys

def search_states():
    """Connects to the database and lists all states matching the argument, sorted by id ASC"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search_name = sys.argv[4]  # The state name prefix to search for

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create cursor and execute query to search for states starting with the search_name
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cur.execute(query, (search_name + '%',))  # Add % to the search_name for a wildcard search

    # Fetch and print results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()

if __name__ == "__main__":
    search_states()

