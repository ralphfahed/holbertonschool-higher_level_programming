#!/usr/bin/python3
"""Prints the id of a State object with the given name from the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # import Base and State from model_state

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create the database engine
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
                           pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the State with the exact name (SQL injection safe)
    state = session.query(State).filter(State.name == state_name).first()

    # Output result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close session
    session.close()
