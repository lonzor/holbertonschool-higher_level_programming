#!/usr/bin/python3
"""
lists all states using SQLAlchemy
from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state_inst = session.query(State).order_by(State.id).first()
    if state_inst:
        print("{}: {}".format(states.id, states.name))
    else:
        print("Nothing")
    session.close()
