#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""

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

    # Query for the first state whose name starts with 'a'
    state = session.query(State).filter(State.name.like('a%')).order_by(State.id).first()

    # If a state is found, print its id and name, otherwise print "Nothing"
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
