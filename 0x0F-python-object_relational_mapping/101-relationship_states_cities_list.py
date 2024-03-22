#!/usr/bin/python3
"""script that creates the State “California” with the City “San Francisco”
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

    q = session.query(State).order_by(State.id)
    for s in q:
        print(f'{s.id}: {s.name}')
        for c in s.cities:
            print(f'\t{c.id}: {c.name}')
