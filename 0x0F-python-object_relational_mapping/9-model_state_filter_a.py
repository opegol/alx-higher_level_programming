#!/usr/bin/python3
# Script lists all State objects that contain the
# letter a from the database hbtn_0e_6_usa
"""lists all State objects that contain the letter 'a'
    from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    q = session.query(State).filter(State.name.ilike("%a%")).order_by(State.id)
    for s in q:
        print(f'{s.id}: {s.name}')
