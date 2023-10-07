from sqlalchemy import Boolean, Column, Integer, String
from db import Base

class User(Base):
  __tablename__ = 'user'
  id = Column(Integer, primary_key = True, index=True)
  username = Column(String(50), unique=True)
  family = Column(String(50), unique=True)


