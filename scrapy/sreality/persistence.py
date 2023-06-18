import os

import sqlalchemy as db
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Integer, String

Base = declarative_base()


def _retrieve_db_url_with_secrets() -> str:
    user = os.environ['POSTGRES_USER']
    password = os.environ['POSTGRES_PASSWORD']
    database = os.environ['POSTGRES_DB']
    host = os.environ['POSTGRES_HOST']
    port = os.environ['POSTGRES_PORT']
    return f'postgresql://{user}:{password}@{host}:{port}/{database}'


class Advertisements(Base):
    __tablename__ = 'advertisements'
    id = Column(Integer, primary_key=True, autoincrement='auto')
    name = Column(String(100), nullable=False)
    image_url = Column(String(100), nullable=False)
    scraped_hash_id = Column(String(100), nullable=False)


class AdvertisementsDao:

    def __init__(self):
        self._engine = db.create_engine(_retrieve_db_url_with_secrets())
        self._session = sessionmaker(self._engine)

    def count(self) -> int:
        with self._session() as session:
            return session.query(Advertisements.id).count()

    def save(self, advertisement: Advertisements) -> None:
        with self._session() as session:
            session.add(advertisement)
            session.commit()
