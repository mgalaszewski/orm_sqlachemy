import sqlalchemy as db
from sqlalchemy.orm import declarative_base, sessionmaker
import config as cf
import logging

engine = db.create_engine(cf.db_address, echo=False)
# connection = engine.connect()
# metadata = db.MetaData()

logging.basicConfig(
    filename='C:\\Users\\micha\\OneDrive\\Pulpit\\keys\\logs\\debug.log',
    level=logging.DEBUG)

Session = sessionmaker(bind=engine)
Base = declarative_base()