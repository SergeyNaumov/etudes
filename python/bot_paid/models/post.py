from sqlalchemy import Boolean, Column, Integer, String, Text
from db import Base

class Post(Base):
  __tablename__ = 'post'
  id = Column(Integer, primary_key = True, index=True)
  header = Column(String(50), unique=True)
  body = Column(Text)
  user_id = Column(Integer)
