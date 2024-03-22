#!/usr/bin/python3
# Script prints all City objects from the database hbtn_0e_14_usa
"""Prints all City objects from the database hbtn_0e_14_usa."""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    q = session.query(State.name, City.id, City.name).join(State). \
        filter(City.state_id == State.id).order_by(City.id)
    for s in q:
        print(f'{s[0]}: ({s[1]}) {s[2]}')
