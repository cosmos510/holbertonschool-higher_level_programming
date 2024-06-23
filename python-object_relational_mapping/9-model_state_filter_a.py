#!/usr/bin/python3
"""
Lists all State objects that contain the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for states containing the letter 'a'
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(
        State.id).all()

    # Print results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
