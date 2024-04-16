from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import Settings



db = Settings().sqlite_db_name
engine = create_engine('postgresql+psycopg2://postgres:password@0.0.0.0:5432/pomodoro')
session = sessionmaker(engine)

def get_db_session():
    return session
