#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa
Usage: ./5-filter_cities.py <username> <password> <database> <state_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    username, password, db_name, state_name = sys.argv[1:5]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create cursor
    cursor = db.cursor()

    # Execute a parameterized query to prevent SQL injection
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch and print results
    rows = cursor.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    # Clean up
    cursor.close()
    db.close()
