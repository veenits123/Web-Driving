from flask import request

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


def GetURL():

    if 'browser' in request.args:
        browser_name = str(request.args['browser'])
        print(browser_name)

        if browser_name == "chrome":

            engine = create_engine(
                'sqlite:////Users/vee_nits123/Library/Application Support/Google/Chrome/Default/History', echo=True)
            Base = declarative_base(engine)

            class url(Base):
                __tablename__ = 'urls'
                __table_args__ = {'autoload': True}

            def loadSession():
                Session = sessionmaker(bind=engine)
                session = Session()
                return session

            session = loadSession()
            res = session.query(url).all()
            ans = res[-1].url
            return ans

        elif browser_name == "mozilla":

            engine = create_engine(
                'sqlite:////Users/vee_nits123/Library/Application Support/Firefox/Profiles/9osmren4.Work Profile/places.sqlite', echo=True)
            Base = declarative_base(engine)

            class url(Base):
                __tablename__ = 'moz_places'
                __table_args__ = {'autoload': True}

            def loadSession():
                Session = sessionmaker(bind=engine)
                session = Session()
                return session

            session = loadSession()
            res = session.query(url).all()
            ans = res[-1].url
            return ans

        else:
            return "Not a Browser!"

    else:
        return "No query passed for filtration"
