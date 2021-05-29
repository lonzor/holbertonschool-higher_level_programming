#!/usr/bin/python3
"""
Lists all states from database hbtn_0e_0_usa
"""


from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host = "localhost", user = argv[1],
                         passwd = argv[2], db = argv[3])
    cur = db.cursor()
    cur.execute("SELECT * from states ORDER BY states.id")
    state_rows = cur.fetchall()
    for state in state_rows:
        print(state)
    cur.close()
    db.close()