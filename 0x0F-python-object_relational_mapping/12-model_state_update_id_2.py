#!/usr/bin/python3
'''
script that lists the all State objects with the letter "a"
 from the database hbtn_0e_6_usa
'''

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    if len(sys.argv) == 4:
        connection = "mysql://{}:{}@localhost:3306/{}".\
                         format(sys.argv[1], sys.argv[2], sys.argv[3])
        engine = create_engine(connection)
        Base.metadata.bind = engine
        SESSION = sessionmaker(bind=engine)
        session = SESSION()
        new_state = session.query(State).filter(State.id == 2).first()
        new_state.name = "New Mexico"
        session.commit()