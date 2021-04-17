import sqlalchemy as db
from datetime import date, timedelta, datetime, timezone as tz
from geoalchemy2 import Geometry
from sqlalchemy import Column, Integer, String, Date, DateTime, JSON, Boolean, BIGINT, ForeignKey, Float, Sequence
from sqlalchemy.orm import declarative_base, sessionmaker
import config as cf
import psycopg2
import logging
from base import Base


class Domains(Base):
    __tablename__ = 'realestates_domain'
    id = Column(BIGINT, Sequence('realestates_domain_id_seq'), primary_key=True)
    create_date = Column('create_date', DateTime)
    update_date = Column('update_date', DateTime, onupdate=datetime.now)
    name = Column('name', String(100))
    values = Column('values', JSON)
    is_active = Column('is_active', Boolean)

    def __init__(self, create_date, name, values, is_active):
        self.create_date = create_date
        self.name = name
        self.values = values
        self.is_active = is_active


class Offers(Base):
    __tablename__ = 'realestates_realestate'
    id = Column(BIGINT, Sequence('realestates_realestate_id_seq'), primary_key=True)
    create_date = Column('create_date', DateTime)
    update_date = Column('update_date', DateTime, onupdate=datetime.now)
    url = Column('name', String(400))
    domain_id = Column(Integer, ForeignKey('realestates_domain.id'))
    offer_title = Column('offer_title', String(500))
    address = Column('address', String(600))
    area = Column('area', Float(8, 17))
    price = Column('price', Float(8, 19))

    def __init__(self, create_date, url, offer_title, address, area, price):
        self.create_date = create_date
        self.url = url
        self.offer_title = offer_title
        self.address = address
        self.area = area
        self.price = price