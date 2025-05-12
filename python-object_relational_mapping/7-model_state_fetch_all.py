#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import Base and State from model_state

if __name__ == "__main__":
    # Get MySQL credentials and database name from command line args
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}", pool_pre_ping=True)

    # Create a session to interact with the DB
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and order by id
    states = session.query(State).order_by(State.id).all()

    # Print results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
