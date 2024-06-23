#!/usr/bin/python3
"""Module compiled with Python3"""

import MySQLdb
import sys

def main():
    """
    Function that lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
    """
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    MY_SEARCH = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, user=MY_USER,
                         passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cur.execute(query, (MY_SEARCH, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
