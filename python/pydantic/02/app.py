from typing import List
# https://sqlmodel.tiangolo.com/tutorial/fastapi/simple-hero-api/ -- изучить

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

#from . import models, schemas
import models, schemas


from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)



db = SessionLocal()


session=Session(engine)
print('session:',session)
records=session.exec(select(Record)).all()
print('records:',session)
quit()
#records = db.query(models.Record).all()
#for r in records:
#    print('r:',r['id'])
#with Session(engine) as session:
records = db.exec(select(Record)).all()
print(records)   

db.close()


def fill_records():
    i=1
    while i<11:
        db_record = models.Record(
            date=f'2022-01-{i}',
            country=f'страна {i}',
            cases=i+1,
            deaths=i+2,
            recoveries=i+3
        )
        db.add(db_record)
        i+=1
    db.commit()

# def get_db():
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()
# app = FastAPI()


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
#     allow_credentials=True,
# )

# # Dependency
# def get_db():
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()


# @app.get("/")
# def main():
#     return RedirectResponse(url="/docs/")


# @app.get("/records/", response_model=List[schemas.Record])
# def show_records(db: Session = Depends(get_db)):
#     records = db.query(models.Record).all()
#     return records