#!/usr/bin/python3
"""
takes in the name of a state as an argument
lists all cities of that state, using the database hbtn_0e_4_usa
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name \
                 FROM cities \
                 INNER JOIN states ON cities.state_id = states.id \
                 WHERE states.name='{:s}' \
                 ORDER BY cities.id ASC".format(argv[4]))
    signal = 0
    city_rows = cur.fetchall()
    for city in city_rows:
        if signal != 0:
            print(", ", end="")
        print("%s" % city, end="")
        signal = signal + 1
    print("")
    cur.close()
    db.close()
