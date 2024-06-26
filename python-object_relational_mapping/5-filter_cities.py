#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306, user=username,
                         passwd=password,
                         db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT cities.name FROM cities JOIN states \
                   ON cities.state_id = states.id WHERE \
                   states.name = %s ORDER BY cities.id ASC", (state_name,))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the results
    print(", ".join(city[0] for city in rows))

    # Close the cursor and database connection
    cursor.close()
    db.close()
