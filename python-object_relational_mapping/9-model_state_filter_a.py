#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_states_with_letter_a(username, password, db_name):
    """
    Lists all State objects that contain the letter a
    from the database specified by username, password, and db_name
    """
    # Create a MySQL engine using SQLAlchemy
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query for states containing the letter 'a' sorted by states.id
    states_with_a = (session.query(State)
                     .filter(State.name.like('%a%'))
                     .order_by(State.id)
                     .all())

    # Display the results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command line arguments
    username, password, db_name = sys.argv[1:4]

    # Call the function with the provided arguments
    list_states_with_letter_a(username, password, db_name)

