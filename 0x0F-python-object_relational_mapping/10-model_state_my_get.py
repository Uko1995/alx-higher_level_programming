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
    if len(sys.argv) == 5:
        connection = "mysql://{}:{}@localhost:3306/{}".\
                         format(sys.argv[1], sys.argv[2], sys.argv[3])
        engine = create_engine(connection)
        Base.metadata.bind = engine
        SESSION = sessionmaker(bind=engine)
        session = SESSION()
        record = session.query(State).filter(State.name == sys.argv[4])\
            .first()

        if record:
            print(f"{record.id}")
        else:
            print("Not found")
