#!/usr/bin/python3
'''
script that deletes the all State objects with the letter "a"
 from the database hbtn_0e_6_usa
'''

from model_state import Base, State
from model_city import City
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
        cities = session.query(City, State).join(State).order_by(City.id)

        for state, city in cities:
            print(f"{city.name}: ({city.id}) {state.name}")
