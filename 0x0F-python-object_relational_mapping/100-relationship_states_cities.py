#!/usr/bin/python3
# script that creates the State “California” with the City “San Francisco”
# from the database hbtn_0e_100_usa
"""creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state_city = City(name='San Francisco', state=State(name='California'))
    session.add(new_state_city)
    session.commit()
