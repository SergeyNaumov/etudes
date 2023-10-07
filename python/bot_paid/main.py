from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from config import config
from typing import Annotated
from sqlalchemy.orm import Session
from db import engine, SessionLocal, Base
import models 



app = FastAPI(Debug=config['debug'])
Base.metadata.create_all(bind=engine)



class PostBase(BaseModel):
  header: str
  body: str
  user_id: int

class UserBase(BaseModel):
  username: str
  family: str

def get_db():
  db = SessionLocal()
  try:
      yield db
  finally:
      db.close()


db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
  db_user = models.User(**user.dict())
  db.add(db_user)
  db.commit()