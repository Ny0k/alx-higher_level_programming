#!/usr/bin/python3
"""script that that prints the State object
    with the name passed as argument from the
    database hbtn_0e_6_usa
"""

from importlib.metadata import metadata
import sys
from model_state import Base, State

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


metadata = MetaData()


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    conn = engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter_by(name=sys.argv[4]).all()

    if len(state) == 0:
        print("Not found")
    else:
        for item in state:
            print(item.id)

    session.close()
    conn.close()
