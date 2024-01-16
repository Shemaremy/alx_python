from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import logging

def list_states(username, password, database):
    # Connect to the MySQL server
    engine = create_engine(f'mysql://{username}:{password}@localhost:3306/{database}')

    # Suppress SQLAlchemy logging
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    # Bind the engine to the Base class
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and display all State objects in ascending order by states.id
    states = session.query(State).order_by(State.id).all()

    # Print the results in the desired format
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    # Check if all three arguments are provided
    import sys
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
    else:
        # Extract arguments
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]

        # Call the function to list all State objects
        list_states(mysql_username, mysql_password, database_name)
