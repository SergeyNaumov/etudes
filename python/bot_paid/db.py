from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import config

engine = create_engine(config['url_database'])

SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base=declarative_base()