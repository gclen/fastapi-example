from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get('/api/teams/', response_model=List[schemas.Team])
def read_teams(db: Session = Depends(get_db)):
    teams = crud.get_all_teams(db)
    return teams

@app.get("/api/wins/{team_id}", response_model=schemas.Team)
def get_team(team_id: int, db: Session = Depends(get_db)):
    team = crud.get_team(db, team_id)
    if team is None:
        raise HTTPException(status_code=404, detail="Team ID not found")
    return team
