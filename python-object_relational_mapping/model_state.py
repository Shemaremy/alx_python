from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """
    State class representing a table in the MySQL database

    Attributes:
    - id: An auto-generated, unique integer representing the primary key
          It can't be null.
    - name: A string with a maximum of 128 characters representing the state name
            It can't be null.

    Table: states
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Connect to the MySQL server
    engine = create_engine('mysql://<mysql_username>:<mysql_password>@localhost:3306/<database_name>', echo=True)

    # Create the table
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Example: Insert a state into the 'states' table
    new_state = State(name='New York')
    session.add(new_state)
    session.commit()

    # Close the session
    session.close()
