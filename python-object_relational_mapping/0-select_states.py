#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)
    
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )
        
        # Create cursor to execute queries
        cursor = db.cursor()
        
        # Execute the query to retrieve all states sorted by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        
        # Fetch all results
        states = cursor.fetchall()
        
        # Display results
        for state in states:
            print(state)
        
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
    finally:
        # Close cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()
