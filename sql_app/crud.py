from sqlalchemy.orm import Session

from . import models, schemas

def get_team(db: Session, team_id: int):
    return db.query(models.Team).filter_by(id=team_id).first()

def get_all_teams(db: Session):
    return db.query(models.Team).order_by(models.Team.team).all()

def get_teams_by_win_count(db: Session, win_count: int):
    return db.query(models.Team).filter_by(wins=win_count).all()