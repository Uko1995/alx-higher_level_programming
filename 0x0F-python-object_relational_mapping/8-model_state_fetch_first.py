#!/usr/bin/python3
'''
script that lists the first State objects from the database hbtn_0e_6_usa
'''

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    if len(sys.argv) == 4:
        connection = f"mysql://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}"
        engine = create_engine(connection)
        Base.metadata.bind = engine
        SESSION = sessionmaker(bind=engine)
        session = SESSION()
        first_state = session.query(State).order_by(State.id).first()

        if first_state:
            print(f"{first_state.id}: {first_state.name}")
        else:
            print('Nothing')
