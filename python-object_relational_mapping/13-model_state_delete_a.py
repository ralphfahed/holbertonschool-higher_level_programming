#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter 'a'"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import your model

if __name__ == "__main__":
    # Get MySQL credentials and DB name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the database
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects with names containing 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each matching state
    for state in states_with_a:
        session.delete(state)

    # Commit the changes to apply deletions
    session.commit()

    # Close the session
    session.close()
