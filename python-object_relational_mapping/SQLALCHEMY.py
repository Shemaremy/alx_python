from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database engine, which wont require mysql to save these data, instead it's own engine
engine = create_engine('sqlite:///:memory:', echo=True)

# Create a declarative base
Base = declarative_base()

# Define a simple User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add a user to the database
new_user = User(name='John Doe', age=25)

session.add(new_user)
session.commit()

# Query the database
query_result = session.query(User).filter_by(name='John Doe').first()
print(query_result.name, query_result.age)

# Close the session
session.close()

