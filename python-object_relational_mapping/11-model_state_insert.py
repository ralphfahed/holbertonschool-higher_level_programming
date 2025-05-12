#!/usr/bin/python3
"""Adds the State object 'Louisiana' to the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import Base and State

if __name__ == "__main__":
    # MySQL credentials and database name from arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create the engine (connection to MySQL)
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
                           pool_pre_ping=True)

    # Create a configured "Session" class and session instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new object to the session and commit to insert into DB
    session.add(new_state)
    session.commit()

    # Print the new state's id
    print(new_state.id)

    # Close the session
    session.close()
