#!/usr/bin/python3
"""
write a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
safe from MySQL injections
"""


from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * from states \
                 WHERE name LIKE %s \
                 ORDER BY states.id ASC", (argv[4],))
    state_rows = cur.fetchall()
    for state in state_rows:
        print(state)
    cur.close()
    db.close()
