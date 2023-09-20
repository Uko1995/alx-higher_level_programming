#!/usr/bin/python3
'''
script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
'''

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    if len(sys.argv) == 4:
        with MySQLdb.connect(host="localhost",
                             user=username,
                             password=password, database=database_name,
                             port=3306) as database:

            cursor = database.cursor()

            query = "SELECT * FROM states WHERE name like binary 'N%' \
                ORDER BY id ASC"
            cursor.execute(query)

            states = cursor.fetchall()

            for state in states:
                print(state)
