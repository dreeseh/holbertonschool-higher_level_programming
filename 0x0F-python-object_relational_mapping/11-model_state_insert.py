#!/usr/bin/python3
"""a script that adds the State object “Louisiana” to the database"""


def connectToDB():
    """connect to datbase here"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    for state in session.query(State)\
        .filter(State.name == 'Louisiana')\
            .order_by(State.id).all():
        if state:
            print("{}".format(state.id))

    session.commit()
    session.close()

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    connectToDB()
