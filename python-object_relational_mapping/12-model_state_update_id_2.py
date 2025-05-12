#!/usr/bin/python3
"""Changes the name of the State object with id=2 to New Mexico"""

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

    # Find the State with id = 2
    state = session.query(State).filter_by(id=2).first()

    if state:
        state.name = "New Mexico"  # Update the name
        session.commit()

    # Close session
    session.close()
