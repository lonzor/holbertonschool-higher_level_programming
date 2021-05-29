#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""


from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd="qp10wo29", db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * from states \
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC")
    state_rows = cur.fetchall()
    for state in state_rows:
        print(state)
    cur.close()
    db.close()