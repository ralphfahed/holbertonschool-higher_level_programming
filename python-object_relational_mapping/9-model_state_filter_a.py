#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a' from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # import State and Base

if __name__ == "__main__":
    # Get credentials from command line args
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Set up the connection to the database
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states with 'a' in the name, ordered by id
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
