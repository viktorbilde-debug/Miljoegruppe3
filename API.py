from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select, MetaData, Table

metadata_obj = MetaData()

engine = create_engine("postgresql+psycopg://app:test@localhost:5432/data_db", echo=True)

humidity = Table("humidity", metadata_obj, autoload_with=engine)

app=FastAPI()

@app.get("/")
def read_hero():
    with Session(engine) as session:
        result = session.exec(select(humidity))
        data = result.mappings().all()



#def read_heroes():
    #with Session(engine) as session:
        #heroes = session.exec(select(Hero)).all()
        #return heroes