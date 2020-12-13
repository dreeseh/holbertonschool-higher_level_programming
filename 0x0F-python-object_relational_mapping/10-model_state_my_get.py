#!/usr/bin/python3
"""prints the first State object from the database"""


def connectToDB():
    """connection happens here"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    found = 0
    for state in session.query(State)\
        .filter(State.name == sys.argv[4],)\
            .order_by(State.id).all():
        if state:
            print("{}".format(state.id))
            found = 1

    if not found:
        print("Not found")

    session.close()


if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    connectToDB()
