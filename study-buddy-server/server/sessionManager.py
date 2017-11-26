from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = "sqlite:///studyBuddyDB.db"

# Thiss handles all of the open/close/commit of the database
# to make sure everything is handled safely.


@contextmanager
def sessionScope(file=None):
    if file is None:
        file = engine
    db = create_engine(file)
    Session = sessionmaker(bind=db)
    session = Session()

    try:
        yield session
        session.commit()
    except Exception, e:
        print "error occured, rolling back:"
        print e
        session.rollback()
        raise
    finally:
        session.close()


def createSession(file=None):
    if file is None:
        file = engine
    db = create_engine(file)
    Session = sessionmaker(bind=db)
    session = Session()
    return session
