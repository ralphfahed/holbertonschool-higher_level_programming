#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import State from model_state
from model_city import City  # Import City from model_city

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

    # Query all cities ordered by cities.id
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Print the results in the format: <state name>: (<city id>) <city name>
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
