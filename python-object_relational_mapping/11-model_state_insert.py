#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create the engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name))

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new state to the session
    session.add(new_state)

    # Commit the session to persist the changes
    session.commit()

    # Print the new state's id
    print(new_state.id)

    session.close()
