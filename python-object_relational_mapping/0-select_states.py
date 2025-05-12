import sys
import MySQLdb

if __name__ == "__main__":
    # Step 1: Get arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Step 2: Connect to MySQL
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Step 3: Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Step 4: Execute the SQL query
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    # Step 5: Fetch the results
    rows = cursor.fetchall()

    # Step 6: Print the results
    for row in rows:
        print(row)

    # Step 7: Close the cursor and connection
    cursor.close()
    connection.close()
