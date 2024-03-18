#!/usr/bin/python3
# script that prints the State object with the name passed
# as argument from the database

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

    q = session.query(State)
    f = 0
    for s in q:
        if s.name == sys.argv[4]:
            print(f'{s.id}')
            f = 1
            break
    if f == 0:
        print('Not found')
