#!/usr/bin/python3
'''
script that lists all states from the database hbtn_0e_0_usa
'''

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    if len(sys.argv) == 5:
        with MySQLdb.connect(host="localhost",
                             user=username,
                             password=password, database=database_name,
                             port=3306) as database:

            cursor = database.cursor()

            query = "SELECT cities.id, cities.name FROM cities \
                INNER JOIN states ON cities.state_id = states.id WHERE \
                states.name = %s ORDER BY cities.id"
            cursor.execute\
                (query, (state_name,))

            states = cursor.fetchall()

            for state in states:
                print(state, end="")
