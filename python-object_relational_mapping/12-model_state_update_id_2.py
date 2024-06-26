#!/usr/bin/python3
"""
Script that changes the name of a State
object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    # Create a configured Session class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the State object with id = 2
    state = session.query(State).filter_by(id=2).first()

    # Change the name of the State to New Mexico
    state.name = "New Mexico"

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
